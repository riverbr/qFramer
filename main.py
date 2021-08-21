import sys
import os
import time
from pathlib import Path
from qt_core import *
from CustomBox import *
from gui.windows.ui_main_window import *
from video_processing import ExtractFrames
from about import AboutApp


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_minimize.clicked.connect(self.showMinimized)
        self.extract_frames = None
        self.thread = None
        self.ui.btn_maximize.setIcon(QIcon(u":/system_icons/img/maximize.png"))
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui.btn_maximize.clicked.connect(self.resize_window)
        self.ui.btn_open_video.clicked.connect(self.open_video_file)
        self.ui.btn_open_frames_dir.clicked.connect(self.select_frames_dir)
        self.ui.top_bar.mousePressEvent = self.top_bar_click
        self.ui.top_bar.mouseMoveEvent = self.drag_window
        self.ui.top_bar.mouseDoubleClickEvent = self.resize_window
        self.ui.btn_extract.clicked.connect(self.start_extraction)
        self.ui.btn_about.clicked.connect(self.about_app)
        self.ui.btn_cancel.clicked.connect(self.abort_extraction)
        self.ui.progress_bar.hide()
        self.ui.btn_cancel.hide()
        self.ui.btn_close.clicked.connect(self.close_app)
        self.maximized = False
        self.about_window = AboutApp()

        self.show()

    def open_video_file(self):
        files_filter = "Video files (*.mp4 *.mkv *.webm *.avi)"
        video_file = QFileDialog.getOpenFileName(self, "Open Video", QDir.homePath(), files_filter)
        self.ui.video_directory.setText(
            video_file[0]
        )

    def select_frames_dir(self):
        self.ui.frames_directory.setText(
            QFileDialog.getExistingDirectory(self,
                                             "Select Directory",
                                             QDir.homePath(),
                                             QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        )

    def validate_video_file(self):
        return_value = True
        message_box = BoxError()
        video_file = self.extract_frames.video_file_name
        is_file = os.path.isfile(video_file)
        if not is_file:
            message_box.setText("Select a valid video file.")
            message_box.exec()
            self.ui.video_directory.setFocus()
            return_value = False
        return return_value

    def validate_frames_dir(self):
        return_value = True
        frames_dir = self.extract_frames.frames_dir
        file_name = f"{frames_dir}/frame0.jpg"
        file = Path(file_name)
        is_abs = os.path.isabs(frames_dir)
        if is_abs:
            message_box = BoxYesNo()
            if file.exists():
                message_box.setText(
                    "There are extracted frames in this directory. Overwrite them?"
                )
                message_box.exec_()
                if message_box.clickedButton() != message_box.button_yes:
                    return_value = False
            if not os.path.exists(frames_dir):
                return_value = False
                message_box.setText("Folder doesn't exist. Create folder?")
                message_box.exec_()
                if message_box.clickedButton() == message_box.button_yes:
                    os.makedirs(frames_dir, 0o777)
                    return_value = True
        else:
            message_box = BoxError()
            message_box.setText("Select a valid directory.")
            message_box.exec()
            self.ui.frames_directory.setFocus()
            return_value = False
        return return_value

    def start_extraction(self):
        self.extract_frames = ExtractFrames()
        self.extract_frames.video_file_name = self.ui.video_directory.text()
        self.extract_frames.frames_dir = self.ui.frames_directory.text()
        if self.validate_video_file() and self.validate_frames_dir():
            self.ui.btn_extract.setEnabled(False)
            self.extract_frames.load_video()
            self.thread = QThread()
            self.extract_frames.moveToThread(self.thread)
            self.thread.started.connect(self.extract_frames.extract)
            self.extract_frames.finished.connect(self.thread.quit)
            self.extract_frames.finished.connect(self.extract_frames.deleteLater)
            self.thread.finished.connect(self.thread.deleteLater)
            self.thread.finished.connect(self.finish_extraction)
            self.thread.start()
            self.ui.btn_cancel.show()
            self.update_progress_bar()

    def update_progress_bar(self):
        frame_count = self.extract_frames.frame_count
        self.ui.progress_bar.setRange(0, frame_count)
        self.ui.progress_bar.show()
        while self.extract_frames.count < frame_count and not self.extract_frames.thread_stopped:
            self.ui.progress_bar.setValue(self.extract_frames.count)
            QApplication.processEvents()
            time.sleep(0.01)

    def finish_extraction(self):
        self.ui.btn_extract.setEnabled(True)
        self.ui.progress_bar.hide()
        self.ui.btn_cancel.hide()
        if not self.extract_frames.thread_stopped:
            message_box = BoxInformation()
            message_box.setText("Extraction completed.")
            message_box.exec_()
        self.thread = None

    def abort_extraction(self):
        self.extract_frames.wait_abort_confirmation(True)
        message_box = BoxYesNo()
        message_box.setText("Abort extraction?")
        message_box.exec_()
        if message_box.clickedButton() == message_box.button_yes:
            self.force_terminate_thread()
            message_box = BoxInformation()
            message_box.setText("Extraction aborted.")
            message_box.exec_()
        self.extract_frames.wait_abort_confirmation(False)

    def top_bar_click(self, event):
        self.oldPos = event.globalPos()

    def drag_window(self, event):
        if self.maximized:
            cursor_pos = QCursor.pos()
            window_half_width = self.minimumWidth() / 2
            self.resize_window(self)
            self.move(cursor_pos.x() - window_half_width, cursor_pos.y())
        else:
            delta = QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()

    def resize_window(self, event):
        if self.isMaximized():
            self.ui.btn_maximize.setIcon(QIcon(u":/system_icons/img/maximize.png"))
            self.showNormal()
            self.maximized = False
        else:
            self.ui.btn_maximize.setIcon(QIcon(u":/system_icons/img/minimize.png"))
            self.showMaximized()
            self.maximized = True

    def force_terminate_thread(self):
        if self.thread.isRunning():
            self.extract_frames.wait_abort_confirmation(False)
            self.extract_frames.stop()
            self.thread.terminate()
            self.thread.wait()

    def close_app(self):
        if self.thread is not None:
            self.force_terminate_thread()
        app.quit()

    def about_app(self):
        if not self.about_window.isVisible():
            self.about_window = AboutApp()
        self.about_window.show()
        self.about_window.activateWindow()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    app.setApplicationName("qFramer")
    window = MainWindow()
    sys.exit(app.exec_())

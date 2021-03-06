import sys
import os
import time
import glob
from pathlib import Path
from qt_core import *
from CustomBox import *
from gui.py_files.ui_main_window import *
from video_processing import ExtractFrames
from about import AboutApp


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_minimize.clicked.connect(self.showMinimized)
        self.extract_frames = ExtractFrames()
        self.thread = None
        self.video_file = None
        self.single_click = False
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui.btn_maximize.setIcon(QIcon(u":/system_icons/img/maximize.png"))
        self.ui.btn_maximize.clicked.connect(lambda: self.resize_window(QEvent, dblClick=True))
        self.ui.btn_open_video.clicked.connect(self.open_video_file)
        self.ui.btn_open_frames_dir.clicked.connect(self.select_frames_dir)
        self.ui.top_bar.mousePressEvent = self.top_bar_click
        self.ui.top_bar.mouseMoveEvent = self.drag_window
        self.ui.top_bar.mouseDoubleClickEvent = self.resize_window
        self.ui.btn_extract.clicked.connect(self.start_extraction)
        self.ui.btn_about.clicked.connect(self.about_app)
        self.ui.ckResize.clicked.connect(self.resize_video)
        self.ui.btn_cancel.clicked.connect(self.abort_extraction)
        self.ui.progress_bar.hide()
        self.ui.btn_cancel.hide()
        self.ui.btn_close.clicked.connect(self.close_app)
        self.about_window = AboutApp()

        self.show()

    def open_video_file(self):
        files_filter = "Video files (*.mp4 *.mkv *.webm *.avi)"
        self.video_file = QFileDialog.getOpenFileName(self, "Open Video", QDir.homePath(), files_filter)
        if self.video_file[0]:
            self.ui.video_directory.setText(self.video_file[0])
            self.extract_frames.load_video(self.video_file[0])
            self.ui.sbWidth.setValue(self.extract_frames.og_width)
            self.ui.sbHeight.setValue(self.extract_frames.og_height)

    def select_frames_dir(self):
        self.ui.frames_directory.setText(
            QFileDialog.getExistingDirectory(self,
                                             "Select Directory",
                                             QDir.homePath(),
                                             QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        )

    def resize_video(self):
        resize = self.ui.ckResize.isChecked()
        if resize:
            self.ui.sbWidth.setEnabled(resize)
            self.ui.sbHeight.setEnabled(resize)
        else:
            self.ui.sbWidth.setEnabled(resize)
            self.ui.sbHeight.setEnabled(resize)
        return resize

    def get_resize_dimensions(self):
        self.extract_frames.resize_width = self.ui.sbWidth.value()
        self.extract_frames.resize_height = self.ui.sbHeight.value()

    def validate_video_file(self):
        ret = True
        message_box = BoxError()
        is_file = os.path.isfile(self.video_file)
        if not is_file:
            message_box.setText("Select a valid video file.")
            message_box.exec()
            self.ui.video_directory.setFocus()
            ret = False
        return ret

    def validate_frames_dir(self):
        ret = True
        frames_dir = self.extract_frames.frames_dir
        is_abs = os.path.isabs(frames_dir)
        if is_abs:
            to_create_folder = False
            confirm_dialog = True
            file_list = glob.glob(f"{frames_dir}/frame*.jpg")
            message_box = BoxYesNo()
            if not os.path.exists(frames_dir):
                to_create_folder = True 
                message_box.setText("Folder doesn't exist. Create folder?")
                message_box.exec_()
            elif len(file_list) > 0:
                message_box.setText("There are extracted frames in this directory. Overwrite them?")
                message_box.exec_()
            else:
                confirm_dialog = False
            if confirm_dialog:
                if message_box.clickedButton() == message_box.button_yes:
                    if to_create_folder:
                        os.makedirs(frames_dir, 0o777)
                else:
                    ret = False
        else:
            ret = False
            message_box = BoxError()
            message_box.setText("Select a valid directory.")
            message_box.exec()
            self.ui.frames_directory.setFocus()
        return ret

    def start_extraction(self):
        self.video_file = self.ui.video_directory.text()
        self.extract_frames.frames_dir = self.ui.frames_directory.text()
        if self.validate_video_file() and self.validate_frames_dir():
            self.ui.btn_extract.setEnabled(False)
            self.extract_frames.resize = self.resize_video()
            if self.extract_frames.resize:
                self.get_resize_dimensions()
            if not self.extract_frames.vidcap:
                self.extract_frames.load_video(self.video_file)
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
            self.extract_frames = ExtractFrames()

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
        self.single_click = True

    def drag_window(self, event):
        if self.single_click:
            if self.isMaximized():
                cursor_pos = QCursor.pos()
                window_half_width = self.minimumWidth() / 2
                self.resize_window(self, dblClick=False)
                self.move(cursor_pos.x() - window_half_width, cursor_pos.y())
            else:
                delta = QPoint(event.globalPos() - self.oldPos)
                self.move(self.x() + delta.x(), self.y() + delta.y())
                self.oldPos = event.globalPos()

    def resize_window(self, event, dblClick=True):
        if dblClick:
            self.single_click = False
        if self.isMaximized():
            self.ui.btn_maximize.setIcon(QIcon(u":/system_icons/img/maximize.png"))
            self.showNormal()
        else:
            self.ui.btn_maximize.setIcon(QIcon(u":/system_icons/img/minimize.png"))
            self.showMaximized()

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

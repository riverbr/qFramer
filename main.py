import sys
import threading
import os

from qt_core import *
from BoxError import BoxError
from gui.windows.ui_main_window import *
from video_processing import ExtractFrames


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.extract_frames = ExtractFrames()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui.btn_open_video.clicked.connect(self.open_video_file)
        self.ui.btn_open_frames_dir.clicked.connect(self.select_frames_dir)
        self.ui.top_bar.mousePressEvent = self.click_on_frame
        self.ui.top_bar.mouseMoveEvent = self.drag_window
        self.ui.top_bar.mouseDoubleClickEvent = self.resize_window
        self.ui.btn_extract.clicked.connect(self.start_extraction)
        self.ui.progress_bar.hide()
        self.maximized = False

        self.show()

    def open_video_file(self):
        files_filter = "Video files (*.mp4, *.mkv, *.avi, *.webm)"
        self.extract_frames.video_file = QFileDialog.getOpenFileName(self, "Open Video", QDir.homePath(), files_filter)
        self.extract_frames.video_file_name = self.extract_frames.video_file[0]
        self.ui.video_directory.setText(self.extract_frames.video_file[0])

    def select_frames_dir(self):
        self.extract_frames.frames_dir = QFileDialog.getExistingDirectory(self, "Select Directory", QDir.homePath(),
                                                                          QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        self.ui.frames_directory.setText(self.extract_frames.frames_dir)

    def validate_file_dir(self):
        message_box = BoxError()
        is_file = os.path.isfile(self.extract_frames.video_file_name)
        is_dir = os.path.isdir(self.extract_frames.frames_dir)
        if not is_file:
            message_box.setText("Select a valid video file.")
            message_box.exec()
            self.ui.video_directory.setFocus()
            return False
        if not is_dir:
            message_box.setText("Select a valid directory.")
            message_box.exec()
            self.ui.frames_directory.setFocus()
            return False
        return True

    def start_extraction(self):
        if self.validate_file_dir():
            self.extract_frames.thread_extraction()
        # self.ui.progress_bar.setMaximum(self.extract_frames.frame_count)
        # self.set_bar_value()

    def set_bar_value(self):
        print(self.ui.progress_bar.value())

    def click_on_frame(self, event):
        self.oldPos = event.globalPosition().toPoint()

    def drag_window(self, event):
        if self.maximized:
            cursor_pos = QCursor.pos()
            window_half_width = self.minimumWidth() / 2
            self.resize_window(self)
            self.move(cursor_pos.x() - window_half_width, cursor_pos.y())
        else:
            delta = QPoint(event.globalPosition().toPoint() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPosition().toPoint()

    def resize_window(self, event):
        if self.isMaximized():
            self.showNormal()
            self.maximized = False
        else:
            self.showMaximized()
            self.maximized = True


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MainWindow()
    sys.exit(app.exec())

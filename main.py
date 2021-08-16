import sys
import os

from qt_core import *

from gui.windows.ui_main_window import *
from video_processing import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui.btn_open_video.clicked.connect(self.open_video_file)
        self.ui.btn_open_frames_dir.clicked.connect(self.select_frames_dir)
        self.ui.top_bar.mousePressEvent = self.click_on_frame
        self.ui.top_bar.mouseMoveEvent = self.drag_window
        self.ui.top_bar.mouseDoubleClickEvent = self.resize_window
        self.ui.btn_extract.clicked.connect(extract_frames)
        self.maximized = False

        self.show()

    def open_video_file(self):
        video_file = QFileDialog.getOpenFileName(self, "Open Video", QDir.homePath(), "MP4 (*.mp4)")
        self.ui.video_directory.setText(video_file[0])

    def select_frames_dir(self):
        frames_dir = QFileDialog.getExistingDirectory(self, "Select Directory", QDir.homePath(),
                                                      QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        self.ui.frames_directory.setText(frames_dir)

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

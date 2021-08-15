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

        self.show()

    def open_video_file(self):
        video_file = QFileDialog.getOpenFileName(self, "Open Video", QDir.homePath(), "MP4 (*.mp4)")
        self.ui.video_directory.setText(video_file[0])

    def select_frames_dir(self):
        frames_dir = QFileDialog.getExistingDirectory(self, "Select Directory", QDir.homePath(),
                                                      QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        self.ui.frames_directory.setText(frames_dir)

    def mousePressEvent(self, event):
        self.oldPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPosition().toPoint() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPosition().toPoint()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MainWindow()
    sys.exit(app.exec())

import cv2
from qt_core import *


class ExtractFrames(QObject):
    finished = Signal()
    progress = Signal(int)

    def __init__(self):
        super().__init__()

        self.video_file = ""
        self.video_file_name = ""
        self.frames_dir = ""
        self.frame_count = 0
        self.count = 0

    def load_video(self):
        self.frames_dir.replace("\\", "/")
        self.video_name = self.video_file_name
        self.vidcap = cv2.VideoCapture(self.video_name)
        self.frame_count = int(self.vidcap.get(cv2.CAP_PROP_FRAME_COUNT))

    def extract(self):
        success, image = self.vidcap.read()
        self.count = 0
        while success:
            frame_dir_name = f"{self.frames_dir}/frame%d.jpg"
            cv2.imwrite(frame_dir_name % self.count, image)
            success, image = self.vidcap.read()
            self.count += 1
        self.finished.emit()

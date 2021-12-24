import cv2
from qt_core import *


class ExtractFrames(QObject):
    finished = Signal()

    def __init__(self):
        super().__init__()

        self.video_file_name = ""
        self.frames_dir = ""
        self.frame_count = 0
        self.count = 0
        self.thread_stopped = False
        self.abort_confirmation = False
        self.resize = False
        self.og_width = 0
        self.og_height = 0
        self.resize_width = 0
        self.resize_height = 0

    def load_video(self):
        self.frames_dir.replace("\\", "/")
        self.vidcap = cv2.VideoCapture(self.video_file_name)
        self.frame_count = int(self.vidcap.get(cv2.CAP_PROP_FRAME_COUNT))

    def extract(self):
        success, image = self.vidcap.read()
        dim = (self.resize_width, self.resize_height)
        self.count = 0
        while success:
            if self.abort_confirmation:
                continue
            if self.thread_stopped:
                break
            frame_dir_name = f"{self.frames_dir}/frame%d.jpg"
            if self.resize:
                image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
            cv2.imwrite(frame_dir_name % self.count, image)
            success, image = self.vidcap.read()
            self.count += 1
        self.finished.emit()

    def stop(self):
        self.thread_stopped = True

    def wait_abort_confirmation(self, abort):
        self.abort_confirmation = abort


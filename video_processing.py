import cv2
import threading


class ExtractFrames:

    def __init__(self):
        super().__init__()

        self.video_file = ""
        self.frames_dir = ""
        self.frame_count = 0

    def extract(self):
        video_name = self.video_file[0]
        vidcap = cv2.VideoCapture(video_name)
        self.frame_count = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
        print(self.frame_count)
        success, image = vidcap.read()
        count = 0
        while success:
            frame_dir_name = f"{self.frames_dir}/frame%d.jpg"
            cv2.imwrite(frame_dir_name % count, image)
            success, image = vidcap.read()
            # print('Read a new frame: ', success)
            count += 1

    def thread_extraction(self):
        extract_thread = threading.Thread(target=self.extract)
        extract_thread.start()

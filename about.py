from gui.windows.ui_about_window import *


class AboutApp(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_about_window()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui.top_bar.mousePressEvent = self.top_bar_click
        self.ui.top_bar.mouseMoveEvent = self.drag_window

    def top_bar_click(self, event):
        self.oldPos = event.globalPos()

    def drag_window(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()
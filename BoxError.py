from qt_core import *


class BoxError(QMessageBox):
    def __init__(self):
        super(BoxError, self).__init__()
        self.setWindowFlags(Qt.Dialog | Qt.CustomizeWindowHint | Qt.WindowTitleHint)
        self.setIcon(QMessageBox.Warning)
        self.setWindowTitle('Error')
        self.setStandardButtons(QMessageBox.Ok)

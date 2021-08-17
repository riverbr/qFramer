from qt_core import *


class Box(QMessageBox):
    def __init__(self):
        super(Box, self).__init__()
        self.setWindowFlags(Qt.Dialog | Qt.CustomizeWindowHint | Qt.WindowTitleHint)
        self.setStandardButtons(QMessageBox.Ok)


class BoxCompleted(Box):
    def __init__(self):
        super(BoxCompleted, self).__init__()
        self.setIcon(QMessageBox.Information)
        self.setWindowTitle('Success')


class BoxError(Box):
    def __init__(self):
        super(BoxError, self).__init__()
        self.setIcon(QMessageBox.Warning)
        self.setWindowTitle('Error')


class BoxYesNo(Box):
    def __init__(self):
        super(BoxYesNo, self).__init__()
        self.setIcon(QMessageBox.Question)
        self.setWindowTitle('Confirm')
        self.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.button_yes = self.button(QMessageBox.Yes)

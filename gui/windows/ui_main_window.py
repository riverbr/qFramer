# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main_windowbnCNpw.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import rc_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 520)
        MainWindow.setMinimumSize(QSize(900, 520))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.top_bar = QFrame(self.centralwidget)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setMaximumSize(QSize(16777215, 24))
        self.top_bar.setStyleSheet(u"background-color: rgb(60, 60, 60);")
        self.horizontalLayout_3 = QHBoxLayout(self.top_bar)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.top_label = QLabel(self.top_bar)
        self.top_label.setObjectName(u"top_label")
        self.top_label.setMaximumSize(QSize(100, 16777215))
        font = QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.top_label.setFont(font)
        self.top_label.setStyleSheet(u"color: rgb(232, 232, 232);")

        self.horizontalLayout_3.addWidget(self.top_label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.gridLayout_2.addWidget(self.top_bar, 0, 0, 1, 1)

        self.content_area = QFrame(self.centralwidget)
        self.content_area.setObjectName(u"content_area")
        self.content_area.setMinimumSize(QSize(0, 48))
        self.content_area.setStyleSheet(u"background-color: rgb(36, 36, 36);")
        self.content_area.setFrameShape(QFrame.NoFrame)
        self.gridLayout = QGridLayout(self.content_area)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(18)
        self.btn_open_video = QPushButton(self.content_area)
        self.btn_open_video.setObjectName(u"btn_open_video")
        self.btn_open_video.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon = QIcon()
        icon.addFile(u":/buttons/img/glass.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_open_video.setIcon(icon)
        self.btn_open_video.setIconSize(QSize(16, 16))

        self.gridLayout.addWidget(self.btn_open_video, 1, 2, 1, 1)

        self.label_2 = QLabel(self.content_area)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setWeight(50)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.frames_directory = QLineEdit(self.content_area)
        self.frames_directory.setObjectName(u"frames_directory")
        self.frames_directory.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 1px solid white;\n"
"border-radius: 2px;")

        self.gridLayout.addWidget(self.frames_directory, 2, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 0, 1, 3)

        self.video_directory = QLineEdit(self.content_area)
        self.video_directory.setObjectName(u"video_directory")
        self.video_directory.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 1px solid white;\n"
"border-radius: 2px;")

        self.gridLayout.addWidget(self.video_directory, 1, 1, 1, 1)

        self.progress_bar = QProgressBar(self.content_area)
        self.progress_bar.setObjectName(u"progress_bar")
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(36, 36, 36, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(0, 120, 215, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush2)
        brush3 = QBrush(QColor(255, 255, 255, 128))
        brush3.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush2)
        brush4 = QBrush(QColor(255, 255, 255, 128))
        brush4.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush2)
        brush5 = QBrush(QColor(255, 255, 255, 128))
        brush5.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.progress_bar.setPalette(palette)
        self.progress_bar.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.progress_bar.setValue(24)
        self.progress_bar.setTextVisible(True)
        self.progress_bar.setTextDirection(QProgressBar.BottomToTop)

        self.gridLayout.addWidget(self.progress_bar, 3, 1, 1, 1)

        self.btn_open_frames_dir = QPushButton(self.content_area)
        self.btn_open_frames_dir.setObjectName(u"btn_open_frames_dir")
        self.btn_open_frames_dir.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.btn_open_frames_dir.setIcon(icon)
        self.btn_open_frames_dir.setIconSize(QSize(16, 16))

        self.gridLayout.addWidget(self.btn_open_frames_dir, 2, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 0, 1, 3)

        self.label = QLabel(self.content_area)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.content_area, 2, 0, 1, 2)

        self.system_buttons = QFrame(self.centralwidget)
        self.system_buttons.setObjectName(u"system_buttons")
        self.system_buttons.setMaximumSize(QSize(16777215, 24))
        self.system_buttons.setStyleSheet(u"background-color: rgb(60, 60, 60);")
        self.horizontalLayout = QHBoxLayout(self.system_buttons)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.system_buttons)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(32, 0))
        self.btn_minimize.setMaximumSize(QSize(32, 16777215))
        self.btn_minimize.setStyleSheet(u"border: none;")
        icon1 = QIcon()
        icon1.addFile(u":/system_icons/img/remove.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon1)
        self.btn_minimize.setIconSize(QSize(24, 24))
        self.btn_minimize.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_minimize)

        self.btn_maximize = QPushButton(self.system_buttons)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setMinimumSize(QSize(32, 0))
        self.btn_maximize.setMaximumSize(QSize(32, 16777215))
        self.btn_maximize.setStyleSheet(u"border: none;")
        self.btn_maximize.setIconSize(QSize(24, 24))
        self.btn_maximize.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_maximize)

        self.btn_close = QPushButton(self.system_buttons)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(32, 0))
        self.btn_close.setMaximumSize(QSize(32, 16777215))
        self.btn_close.setStyleSheet(u"border: none;")
        icon2 = QIcon()
        icon2.addFile(u":/system_icons/img/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)
        self.btn_close.setIconSize(QSize(24, 24))
        self.btn_close.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_close)


        self.gridLayout_2.addWidget(self.system_buttons, 0, 1, 1, 1)

        self.menu = QFrame(self.centralwidget)
        self.menu.setObjectName(u"menu")
        self.menu.setMaximumSize(QSize(16777215, 48))
        self.menu.setStyleSheet(u"background-color: rgb(60, 60, 60);")
        self.menu.setFrameShape(QFrame.StyledPanel)
        self.menu.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.menu)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_extract = QToolButton(self.menu)
        self.btn_extract.setObjectName(u"btn_extract")
        self.btn_extract.setMinimumSize(QSize(0, 46))
        self.btn_extract.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon3 = QIcon()
        icon3.addFile(u":/menu/img/extract.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_extract.setIcon(icon3)
        self.btn_extract.setIconSize(QSize(32, 32))
        self.btn_extract.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.btn_extract.setAutoRaise(True)
        self.btn_extract.setArrowType(Qt.NoArrow)

        self.horizontalLayout_2.addWidget(self.btn_extract)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.btn_about = QToolButton(self.menu)
        self.btn_about.setObjectName(u"btn_about")
        self.btn_about.setMinimumSize(QSize(0, 46))
        icon4 = QIcon()
        icon4.addFile(u":/menu/img/info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_about.setIcon(icon4)
        self.btn_about.setIconSize(QSize(28, 28))
        self.btn_about.setAutoRaise(True)

        self.horizontalLayout_2.addWidget(self.btn_about)


        self.gridLayout_2.addWidget(self.menu, 1, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.top_label.setText(QCoreApplication.translate("MainWindow", u"qFramer", None))
        self.btn_open_video.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Save Frames to:", None))
        self.btn_open_frames_dir.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Select Video:", None))
        self.btn_minimize.setText("")
        self.btn_maximize.setText("")
        self.btn_close.setText("")
        self.btn_extract.setText(QCoreApplication.translate("MainWindow", u"Extract", None))
        self.btn_about.setText("")
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main_windowVRHjrA.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import rc_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 520)
        MainWindow.setMinimumSize(QSize(900, 520))
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_bar = QFrame(self.centralwidget)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setMaximumSize(QSize(16777215, 24))
        self.top_bar.setStyleSheet(u"background-color: rgb(60, 60, 60);")
        self.top_bar.setFrameShape(QFrame.StyledPanel)
        self.top_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.top_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_label = QLabel(self.top_bar)
        self.top_label.setObjectName(u"top_label")
        self.top_label.setMaximumSize(QSize(100, 16777215))
        font = QFont()
        font.setPointSize(16)
        font.setBold(False)
        self.top_label.setFont(font)
        self.top_label.setStyleSheet(u"color: rgb(232, 232, 232);")

        self.horizontalLayout.addWidget(self.top_label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_close = QPushButton(self.top_bar)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMaximumSize(QSize(24, 16777215))
        self.btn_close.setStyleSheet(u"border: none;")
        icon = QIcon()
        icon.addFile(u":/system_icons/img/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon)
        self.btn_close.setIconSize(QSize(32, 32))
        self.btn_close.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_close)


        self.verticalLayout.addWidget(self.top_bar)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 48))
        self.frame.setStyleSheet(u"background-color: rgb(60, 60, 60);")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_extract = QToolButton(self.frame)
        self.btn_extract.setObjectName(u"btn_extract")
        self.btn_extract.setMinimumSize(QSize(0, 48))
        self.btn_extract.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon1 = QIcon()
        icon1.addFile(u":/menu/img/extract.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_extract.setIcon(icon1)
        self.btn_extract.setIconSize(QSize(32, 32))
        self.btn_extract.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.btn_extract.setAutoRaise(True)
        self.btn_extract.setArrowType(Qt.NoArrow)

        self.horizontalLayout_2.addWidget(self.btn_extract)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.btn_about = QToolButton(self.frame)
        self.btn_about.setObjectName(u"btn_about")
        self.btn_about.setMinimumSize(QSize(0, 48))
        icon2 = QIcon()
        icon2.addFile(u":/menu/img/info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_about.setIcon(icon2)
        self.btn_about.setIconSize(QSize(28, 28))
        self.btn_about.setAutoRaise(True)

        self.horizontalLayout_2.addWidget(self.btn_about)


        self.verticalLayout.addWidget(self.frame)

        self.content_area = QFrame(self.centralwidget)
        self.content_area.setObjectName(u"content_area")
        self.content_area.setStyleSheet(u"background-color: rgb(36, 36, 36);")
        self.content_area.setFrameShape(QFrame.StyledPanel)
        self.content_area.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.content_area)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(18)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 2)

        self.video_directory = QLineEdit(self.content_area)
        self.video_directory.setObjectName(u"video_directory")
        self.video_directory.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 1px solid white;\n"
"border-radius: 2px;")

        self.gridLayout.addWidget(self.video_directory, 0, 1, 1, 1)

        self.frames_directory = QLineEdit(self.content_area)
        self.frames_directory.setObjectName(u"frames_directory")
        self.frames_directory.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 1px solid white;\n"
"border-radius: 2px;")

        self.gridLayout.addWidget(self.frames_directory, 1, 1, 1, 1)

        self.btn_open_video = QPushButton(self.content_area)
        self.btn_open_video.setObjectName(u"btn_open_video")
        self.btn_open_video.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon3 = QIcon()
        icon3.addFile(u":/glass/img/glass.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_open_video.setIcon(icon3)
        self.btn_open_video.setIconSize(QSize(16, 16))

        self.gridLayout.addWidget(self.btn_open_video, 0, 2, 1, 1)

        self.btn_open_frames_dir = QPushButton(self.content_area)
        self.btn_open_frames_dir.setObjectName(u"btn_open_frames_dir")
        self.btn_open_frames_dir.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.btn_open_frames_dir.setIcon(icon3)
        self.btn_open_frames_dir.setIconSize(QSize(16, 16))

        self.gridLayout.addWidget(self.btn_open_frames_dir, 1, 2, 1, 1)

        self.label_2 = QLabel(self.content_area)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label = QLabel(self.content_area)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.content_area)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_close.clicked.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.top_label.setText(QCoreApplication.translate("MainWindow", u"qFramer", None))
        self.btn_close.setText("")
        self.btn_extract.setText(QCoreApplication.translate("MainWindow", u"Extract", None))
        self.btn_about.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_open_video.setText("")
        self.btn_open_frames_dir.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Save Frames to:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Select Video:", None))
    # retranslateUi


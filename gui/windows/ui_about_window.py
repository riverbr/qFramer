# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_about_windowEFdYlE.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import rc_rc

class Ui_about_window(object):
    def setupUi(self, about_window):
        if not about_window.objectName():
            about_window.setObjectName(u"about_window")
        about_window.resize(400, 300)
        about_window.setMinimumSize(QSize(400, 300))
        self.gridLayout = QGridLayout(about_window)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.top_bar = QFrame(about_window)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setMaximumSize(QSize(16777215, 24))
        self.top_bar.setStyleSheet(u"background-color: rgb(60, 60, 60);")
        self.horizontalLayout_2 = QHBoxLayout(self.top_bar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.top_label = QLabel(self.top_bar)
        self.top_label.setObjectName(u"top_label")
        self.top_label.setMaximumSize(QSize(100, 16777215))
        font = QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.top_label.setFont(font)
        self.top_label.setStyleSheet(u"color: rgb(232, 232, 232);")

        self.horizontalLayout_2.addWidget(self.top_label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.gridLayout.addWidget(self.top_bar, 0, 0, 1, 1)

        self.system_buttons = QFrame(about_window)
        self.system_buttons.setObjectName(u"system_buttons")
        self.system_buttons.setMinimumSize(QSize(32, 0))
        self.system_buttons.setMaximumSize(QSize(32, 24))
        self.system_buttons.setStyleSheet(u"background-color: rgb(60, 60, 60);")
        self.horizontalLayout = QHBoxLayout(self.system_buttons)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_close = QPushButton(self.system_buttons)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(32, 0))
        self.btn_close.setMaximumSize(QSize(32, 32))
        self.btn_close.setStyleSheet(u"border: none;")
        icon = QIcon()
        icon.addFile(u":/system_icons/img/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon)
        self.btn_close.setIconSize(QSize(24, 24))
        self.btn_close.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_close)


        self.gridLayout.addWidget(self.system_buttons, 0, 1, 1, 1)

        self.content_area = QFrame(about_window)
        self.content_area.setObjectName(u"content_area")
        self.content_area.setStyleSheet(u"background-color: rgb(36, 36, 36);")
        self.content_area.setFrameShape(QFrame.StyledPanel)
        self.content_area.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.content_area)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.content_area)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(100, 100))
        self.label.setMaximumSize(QSize(100, 100))
        self.label.setPixmap(QPixmap(u":/logo/img/logo.png"))
        self.label.setScaledContents(True)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.lbl_about = QLabel(self.content_area)
        self.lbl_about.setObjectName(u"lbl_about")
        font1 = QFont()
        font1.setFamily(u"Tahoma")
        font1.setPointSize(10)
        self.lbl_about.setFont(font1)
        self.lbl_about.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lbl_about.setWordWrap(True)
        self.lbl_about.setOpenExternalLinks(True)

        self.gridLayout_2.addWidget(self.lbl_about, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.content_area, 1, 0, 1, 2)


        self.retranslateUi(about_window)
        self.btn_close.clicked.connect(about_window.close)

        QMetaObject.connectSlotsByName(about_window)
    # setupUi

    def retranslateUi(self, about_window):
        about_window.setWindowTitle(QCoreApplication.translate("about_window", u"Dialog", None))
        self.top_label.setText(QCoreApplication.translate("about_window", u"About", None))
        self.btn_close.setText("")
        self.label.setText("")
        self.lbl_about.setText(QCoreApplication.translate("about_window", u"<html><head/><body><p>qFramer is a free video frame extraction tool developed in Python, based on Qt toolkit (PySide2) and OpenCV.</p><p>Qt: 5.15.2</p><p>OpenCV 4.5.3.56: </p><p>System Icons by Microsoft on <a href=\"www.iconscout.com\"><span style=\" text-decoration: underline; color:#007acc;\">IconScout</span></a></p></body></html>", None))
    # retranslateUi


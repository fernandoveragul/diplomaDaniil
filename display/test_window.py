# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(536, 478)
        font = QFont()
        font.setPointSize(16)
        Form.setFont(font)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.pgAuth = QWidget()
        self.pgAuth.setObjectName(u"pgAuth")
        self.gridLayout = QGridLayout(self.pgAuth)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_2 = QSpacerItem(149, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 2, 1, 1)

        self.ledtGroupName = QLineEdit(self.pgAuth)
        self.ledtGroupName.setObjectName(u"ledtGroupName")

        self.gridLayout.addWidget(self.ledtGroupName, 3, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 153, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.btnLogin = QPushButton(self.pgAuth)
        self.btnLogin.setObjectName(u"btnLogin")

        self.gridLayout.addWidget(self.btnLogin, 4, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 153, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 5, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(149, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.ledtSecondName = QLineEdit(self.pgAuth)
        self.ledtSecondName.setObjectName(u"ledtSecondName")

        self.gridLayout.addWidget(self.ledtSecondName, 2, 1, 1, 1)

        self.ledtReceiverEMail = QLineEdit(self.pgAuth)
        self.ledtReceiverEMail.setObjectName(u"ledtReceiverEMail")

        self.gridLayout.addWidget(self.ledtReceiverEMail, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.pgAuth)
        self.pgTest = QWidget()
        self.pgTest.setObjectName(u"pgTest")
        self.gridLayout_2 = QGridLayout(self.pgTest)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lblTimer = QLabel(self.pgTest)
        self.lblTimer.setObjectName(u"lblTimer")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblTimer.sizePolicy().hasHeightForWidth())
        self.lblTimer.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Consolas"])
        font1.setPointSize(12)
        self.lblTimer.setFont(font1)
        self.lblTimer.setCursor(QCursor(Qt.WaitCursor))

        self.gridLayout_2.addWidget(self.lblTimer, 0, 0, 1, 1)

        self.progressBar = QProgressBar(self.pgTest)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy1)
        self.progressBar.setCursor(QCursor(Qt.WaitCursor))
        self.progressBar.setValue(24)
        self.progressBar.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.progressBar, 0, 1, 1, 1)

        self.btnFinish = QPushButton(self.pgTest)
        self.btnFinish.setObjectName(u"btnFinish")
        sizePolicy.setHeightForWidth(self.btnFinish.sizePolicy().hasHeightForWidth())
        self.btnFinish.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(12)
        self.btnFinish.setFont(font2)
        self.btnFinish.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnFinish.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_2.addWidget(self.btnFinish, 0, 2, 1, 1)

        self.tbrQuestion = QTextBrowser(self.pgTest)
        self.tbrQuestion.setObjectName(u"tbrQuestion")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tbrQuestion.sizePolicy().hasHeightForWidth())
        self.tbrQuestion.setSizePolicy(sizePolicy2)
        self.tbrQuestion.viewport().setProperty("cursor", QCursor(Qt.ForbiddenCursor))
        self.tbrQuestion.setFrameShape(QFrame.NoFrame)
        self.tbrQuestion.setFrameShadow(QFrame.Plain)

        self.gridLayout_2.addWidget(self.tbrQuestion, 1, 0, 1, 3)

        self.verticalSpacer_3 = QSpacerItem(20, 31, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 2, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(108, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 3, 0, 1, 1)

        self.btnAnswer_1 = QPushButton(self.pgTest)
        self.btnAnswer_1.setObjectName(u"btnAnswer_1")
        font3 = QFont()
        font3.setPointSize(14)
        self.btnAnswer_1.setFont(font3)
        self.btnAnswer_1.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btnAnswer_1, 3, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(116, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 3, 2, 1, 1)

        self.btnAnswer_2 = QPushButton(self.pgTest)
        self.btnAnswer_2.setObjectName(u"btnAnswer_2")
        self.btnAnswer_2.setFont(font3)
        self.btnAnswer_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btnAnswer_2, 4, 1, 1, 1)

        self.btnAnswer_3 = QPushButton(self.pgTest)
        self.btnAnswer_3.setObjectName(u"btnAnswer_3")
        self.btnAnswer_3.setFont(font3)
        self.btnAnswer_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btnAnswer_3, 5, 1, 1, 1)

        self.btnAnswer_4 = QPushButton(self.pgTest)
        self.btnAnswer_4.setObjectName(u"btnAnswer_4")
        self.btnAnswer_4.setFont(font3)
        self.btnAnswer_4.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btnAnswer_4, 6, 1, 1, 1)

        self.stackedWidget.addWidget(self.pgTest)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0422\u0435\u0441\u0442", None))
        self.btnLogin.setText(QCoreApplication.translate("Form", u"\u041d\u0410\u0427\u0410\u0422\u042c \u0422\u0415\u0421\u0422", None))
        self.lblTimer.setText(QCoreApplication.translate("Form", u"00:00:00", None))
        self.btnFinish.setText(QCoreApplication.translate("Form", u"\u0417\u0410\u041a\u041e\u041d\u0427\u0418\u0422\u042c", None))
        self.btnAnswer_1.setText(QCoreApplication.translate("Form", u"\u041d\u0410\u0416\u041c\u0418\u0422\u0415, \u0427\u0422\u041e\u0411\u042b \u041d\u0410\u0427\u0410\u0422\u042c", None))
        self.btnAnswer_2.setText(QCoreApplication.translate("Form", u"\u041d\u0410\u0416\u041c\u0418\u0422\u0415, \u0427\u0422\u041e\u0411\u042b \u041d\u0410\u0427\u0410\u0422\u042c", None))
        self.btnAnswer_3.setText(QCoreApplication.translate("Form", u"\u041d\u0410\u0416\u041c\u0418\u0422\u0415, \u0427\u0422\u041e\u0411\u042b \u041d\u0410\u0427\u0410\u0422\u042c", None))
        self.btnAnswer_4.setText(QCoreApplication.translate("Form", u"\u041d\u0410\u0416\u041c\u0418\u0422\u0415, \u0427\u0422\u041e\u0411\u042b \u041d\u0410\u0427\u0410\u0422\u042c", None))
    # retranslateUi


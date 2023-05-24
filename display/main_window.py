# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPlainTextEdit, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QTabWidget,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(870, 574)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setPointSize(12)
        self.centralwidget.setFont(font)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackApp = QStackedWidget(self.centralwidget)
        self.stackApp.setObjectName(u"stackApp")
        self.pgStart = QWidget()
        self.pgStart.setObjectName(u"pgStart")
        self.gridLayout_2 = QGridLayout(self.pgStart)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer_5 = QSpacerItem(20, 101, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_5, 0, 1, 1, 1)

        self.btnStartApp = QPushButton(self.pgStart)
        self.btnStartApp.setObjectName(u"btnStartApp")
        self.btnStartApp.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btnStartApp, 4, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 4, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 101, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 3, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 101, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 5, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 4, 2, 1, 1)

        self.tbrSummaryApp = QTextBrowser(self.pgStart)
        self.tbrSummaryApp.setObjectName(u"tbrSummaryApp")
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.tbrSummaryApp.setFont(font1)
        self.tbrSummaryApp.setFrameShape(QFrame.NoFrame)
        self.tbrSummaryApp.setFrameShadow(QFrame.Plain)
        self.tbrSummaryApp.setLineWidth(1)

        self.gridLayout_2.addWidget(self.tbrSummaryApp, 2, 0, 1, 3)

        self.stackApp.addWidget(self.pgStart)
        self.pgApp = QWidget()
        self.pgApp.setObjectName(u"pgApp")
        self.verticalLayout_7 = QVBoxLayout(self.pgApp)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.pgApp)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tbStudent = QWidget()
        self.tbStudent.setObjectName(u"tbStudent")
        self.verticalLayout_3 = QVBoxLayout(self.tbStudent)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stckStudent = QStackedWidget(self.tbStudent)
        self.stckStudent.setObjectName(u"stckStudent")
        self.pgTutorial = QWidget()
        self.pgTutorial.setObjectName(u"pgTutorial")
        self.gridLayout = QGridLayout(self.pgTutorial)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.btnShowExample = QPushButton(self.pgTutorial)
        self.btnShowExample.setObjectName(u"btnShowExample")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnShowExample.sizePolicy().hasHeightForWidth())
        self.btnShowExample.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btnShowExample, 2, 0, 1, 1)

        self.btnShowMethodist = QPushButton(self.pgTutorial)
        self.btnShowMethodist.setObjectName(u"btnShowMethodist")
        sizePolicy.setHeightForWidth(self.btnShowMethodist.sizePolicy().hasHeightForWidth())
        self.btnShowMethodist.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btnShowMethodist, 1, 0, 1, 1)

        self.pdfTutorial = QWebEngineView(self.pgTutorial)
        self.pdfTutorial.setObjectName(u"pdfTutorial")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(5)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pdfTutorial.sizePolicy().hasHeightForWidth())
        self.pdfTutorial.setSizePolicy(sizePolicy1)
        self.pdfTutorial.setUrl(QUrl(u"about:blank"))

        self.gridLayout.addWidget(self.pdfTutorial, 0, 1, 3, 1)

        self.scrollTutorial = QScrollArea(self.pgTutorial)
        self.scrollTutorial.setObjectName(u"scrollTutorial")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scrollTutorial.sizePolicy().hasHeightForWidth())
        self.scrollTutorial.setSizePolicy(sizePolicy2)
        self.scrollTutorial.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.scrollTutorial.setWidgetResizable(True)
        self.areaTutorial = QWidget()
        self.areaTutorial.setObjectName(u"areaTutorial")
        self.areaTutorial.setGeometry(QRect(0, 0, 237, 467))
        self.layTutorial = QVBoxLayout(self.areaTutorial)
        self.layTutorial.setObjectName(u"layTutorial")
        self.scrollTutorial.setWidget(self.areaTutorial)

        self.gridLayout.addWidget(self.scrollTutorial, 0, 0, 1, 1)

        self.stckStudent.addWidget(self.pgTutorial)
        self.pgExample = QWidget()
        self.pgExample.setObjectName(u"pgExample")
        self.gridLayout_3 = QGridLayout(self.pgExample)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(6)
        self.gridLayout_3.setContentsMargins(2, 2, 2, 2)
        self.btnShowTutorial = QPushButton(self.pgExample)
        self.btnShowTutorial.setObjectName(u"btnShowTutorial")
        sizePolicy.setHeightForWidth(self.btnShowTutorial.sizePolicy().hasHeightForWidth())
        self.btnShowTutorial.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.btnShowTutorial, 1, 0, 1, 1)

        self.btnTest = QPushButton(self.pgExample)
        self.btnTest.setObjectName(u"btnTest")
        sizePolicy.setHeightForWidth(self.btnTest.sizePolicy().hasHeightForWidth())
        self.btnTest.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.btnTest, 2, 0, 1, 1)

        self.scrollExample = QScrollArea(self.pgExample)
        self.scrollExample.setObjectName(u"scrollExample")
        sizePolicy2.setHeightForWidth(self.scrollExample.sizePolicy().hasHeightForWidth())
        self.scrollExample.setSizePolicy(sizePolicy2)
        self.scrollExample.setWidgetResizable(True)
        self.areaExample = QWidget()
        self.areaExample.setObjectName(u"areaExample")
        self.areaExample.setGeometry(QRect(0, 0, 64, 18))
        self.layExample = QVBoxLayout(self.areaExample)
        self.layExample.setObjectName(u"layExample")
        self.scrollExample.setWidget(self.areaExample)

        self.gridLayout_3.addWidget(self.scrollExample, 0, 0, 1, 1)

        self.pdfExample = QWebEngineView(self.pgExample)
        self.pdfExample.setObjectName(u"pdfExample")
        sizePolicy1.setHeightForWidth(self.pdfExample.sizePolicy().hasHeightForWidth())
        self.pdfExample.setSizePolicy(sizePolicy1)
        self.pdfExample.setUrl(QUrl(u"about:blank"))

        self.gridLayout_3.addWidget(self.pdfExample, 0, 1, 3, 1)

        self.stckStudent.addWidget(self.pgExample)
        self.pgMethodist = QWidget()
        self.pgMethodist.setObjectName(u"pgMethodist")
        self.gridLayout_7 = QGridLayout(self.pgMethodist)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(2, 2, 2, 2)
        self.scrollMethodistPr = QScrollArea(self.pgMethodist)
        self.scrollMethodistPr.setObjectName(u"scrollMethodistPr")
        sizePolicy2.setHeightForWidth(self.scrollMethodistPr.sizePolicy().hasHeightForWidth())
        self.scrollMethodistPr.setSizePolicy(sizePolicy2)
        self.scrollMethodistPr.setWidgetResizable(True)
        self.areaMethodist = QWidget()
        self.areaMethodist.setObjectName(u"areaMethodist")
        self.areaMethodist.setGeometry(QRect(0, 0, 74, 18))
        self.layMethodist = QVBoxLayout(self.areaMethodist)
        self.layMethodist.setObjectName(u"layMethodist")
        self.scrollMethodistPr.setWidget(self.areaMethodist)

        self.gridLayout_7.addWidget(self.scrollMethodistPr, 0, 0, 2, 1)

        self.btnGoToStartState = QPushButton(self.pgMethodist)
        self.btnGoToStartState.setObjectName(u"btnGoToStartState")

        self.gridLayout_7.addWidget(self.btnGoToStartState, 2, 0, 1, 1)

        self.pdfMethodist = QWebEngineView(self.pgMethodist)
        self.pdfMethodist.setObjectName(u"pdfMethodist")
        sizePolicy1.setHeightForWidth(self.pdfMethodist.sizePolicy().hasHeightForWidth())
        self.pdfMethodist.setSizePolicy(sizePolicy1)
        self.pdfMethodist.setUrl(QUrl(u"about:blank"))

        self.gridLayout_7.addWidget(self.pdfMethodist, 0, 1, 3, 1)

        self.stckStudent.addWidget(self.pgMethodist)

        self.verticalLayout_3.addWidget(self.stckStudent)

        self.tabWidget.addTab(self.tbStudent, "")
        self.tbProfessor = QWidget()
        self.tbProfessor.setObjectName(u"tbProfessor")
        self.verticalLayout_2 = QVBoxLayout(self.tbProfessor)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackProfessor = QStackedWidget(self.tbProfessor)
        self.stackProfessor.setObjectName(u"stackProfessor")
        self.pgLogin = QWidget()
        self.pgLogin.setObjectName(u"pgLogin")
        self.gridLayout_4 = QGridLayout(self.pgLogin)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalSpacer_3 = QSpacerItem(20, 196, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(249, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.ledtLogin = QLineEdit(self.pgLogin)
        self.ledtLogin.setObjectName(u"ledtLogin")
        self.ledtLogin.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.ledtLogin, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(249, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.ledtPassword = QLineEdit(self.pgLogin)
        self.ledtPassword.setObjectName(u"ledtPassword")
        self.ledtPassword.setEchoMode(QLineEdit.Password)
        self.ledtPassword.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.ledtPassword, 2, 1, 1, 1)

        self.btnLogin = QPushButton(self.pgLogin)
        self.btnLogin.setObjectName(u"btnLogin")
        font2 = QFont()
        font2.setPointSize(14)
        self.btnLogin.setFont(font2)

        self.gridLayout_4.addWidget(self.btnLogin, 3, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 195, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_4, 4, 1, 1, 1)

        self.stackProfessor.addWidget(self.pgLogin)
        self.pgCreate = QWidget()
        self.pgCreate.setObjectName(u"pgCreate")
        self.gridLayout_5 = QGridLayout(self.pgCreate)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gboxFileWorkers = QGroupBox(self.pgCreate)
        self.gboxFileWorkers.setObjectName(u"gboxFileWorkers")
        self.gboxFileWorkers.setFont(font2)
        self.gboxFileWorkers.setFlat(False)
        self.verticalLayout_5 = QVBoxLayout(self.gboxFileWorkers)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.btnAddTutorial = QPushButton(self.gboxFileWorkers)
        self.btnAddTutorial.setObjectName(u"btnAddTutorial")
        self.btnAddTutorial.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.btnAddTutorial)

        self.btnDelTutorial = QPushButton(self.gboxFileWorkers)
        self.btnDelTutorial.setObjectName(u"btnDelTutorial")
        self.btnDelTutorial.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.btnDelTutorial)

        self.btnAddExample = QPushButton(self.gboxFileWorkers)
        self.btnAddExample.setObjectName(u"btnAddExample")
        self.btnAddExample.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.btnAddExample)

        self.btnDelExample = QPushButton(self.gboxFileWorkers)
        self.btnDelExample.setObjectName(u"btnDelExample")
        self.btnDelExample.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.btnDelExample)

        self.btnDelTest = QPushButton(self.gboxFileWorkers)
        self.btnDelTest.setObjectName(u"btnDelTest")

        self.verticalLayout_5.addWidget(self.btnDelTest)

        self.btnAddMethodist = QPushButton(self.gboxFileWorkers)
        self.btnAddMethodist.setObjectName(u"btnAddMethodist")
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(False)
        self.btnAddMethodist.setFont(font3)

        self.verticalLayout_5.addWidget(self.btnAddMethodist)

        self.btnDelMethodist = QPushButton(self.gboxFileWorkers)
        self.btnDelMethodist.setObjectName(u"btnDelMethodist")

        self.verticalLayout_5.addWidget(self.btnDelMethodist)


        self.gridLayout_5.addWidget(self.gboxFileWorkers, 0, 0, 3, 1)

        self.line = QFrame(self.pgCreate)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line, 0, 1, 10, 1)

        self.ledtTimeToDo = QLineEdit(self.pgCreate)
        self.ledtTimeToDo.setObjectName(u"ledtTimeToDo")
        self.ledtTimeToDo.setFont(font2)
        self.ledtTimeToDo.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.ledtTimeToDo, 0, 2, 1, 1)

        self.btnAddQuestion = QPushButton(self.pgCreate)
        self.btnAddQuestion.setObjectName(u"btnAddQuestion")
        self.btnAddQuestion.setFont(font2)

        self.gridLayout_5.addWidget(self.btnAddQuestion, 0, 3, 1, 1)

        self.btnEndCreateTest = QPushButton(self.pgCreate)
        self.btnEndCreateTest.setObjectName(u"btnEndCreateTest")
        self.btnEndCreateTest.setFont(font2)

        self.gridLayout_5.addWidget(self.btnEndCreateTest, 0, 4, 1, 1)

        self.line_3 = QFrame(self.pgCreate)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line_3, 1, 2, 1, 3)

        self.verticalSpacer_9 = QSpacerItem(20, 36, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_9, 3, 0, 1, 1)

        self.line_2 = QFrame(self.pgCreate)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line_2, 4, 0, 1, 1)

        self.line_4 = QFrame(self.pgCreate)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line_4, 4, 2, 1, 3)

        self.groupBox = QGroupBox(self.pgCreate)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font2)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.rbtnAnswerFirst = QRadioButton(self.groupBox)
        self.rbtnAnswerFirst.setObjectName(u"rbtnAnswerFirst")
        self.rbtnAnswerFirst.setCursor(QCursor(Qt.PointingHandCursor))
        self.rbtnAnswerFirst.setChecked(True)

        self.verticalLayout_6.addWidget(self.rbtnAnswerFirst)

        self.rbtnAnswerSecond = QRadioButton(self.groupBox)
        self.rbtnAnswerSecond.setObjectName(u"rbtnAnswerSecond")
        self.rbtnAnswerSecond.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_6.addWidget(self.rbtnAnswerSecond)

        self.rbtnAnswerThird = QRadioButton(self.groupBox)
        self.rbtnAnswerThird.setObjectName(u"rbtnAnswerThird")
        self.rbtnAnswerThird.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_6.addWidget(self.rbtnAnswerThird)

        self.rbtnAnswerFour = QRadioButton(self.groupBox)
        self.rbtnAnswerFour.setObjectName(u"rbtnAnswerFour")
        self.rbtnAnswerFour.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_6.addWidget(self.rbtnAnswerFour)


        self.gridLayout_5.addWidget(self.groupBox, 6, 0, 4, 1)

        self.ledtAnswerFirst = QLineEdit(self.pgCreate)
        self.ledtAnswerFirst.setObjectName(u"ledtAnswerFirst")
        self.ledtAnswerFirst.setFont(font2)
        self.ledtAnswerFirst.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.ledtAnswerFirst, 6, 2, 1, 3)

        self.ledtAnswerSecond = QLineEdit(self.pgCreate)
        self.ledtAnswerSecond.setObjectName(u"ledtAnswerSecond")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.ledtAnswerSecond.sizePolicy().hasHeightForWidth())
        self.ledtAnswerSecond.setSizePolicy(sizePolicy3)
        self.ledtAnswerSecond.setFont(font2)
        self.ledtAnswerSecond.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.ledtAnswerSecond, 7, 2, 1, 3)

        self.ledtAnswerThird = QLineEdit(self.pgCreate)
        self.ledtAnswerThird.setObjectName(u"ledtAnswerThird")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.ledtAnswerThird.sizePolicy().hasHeightForWidth())
        self.ledtAnswerThird.setSizePolicy(sizePolicy4)
        self.ledtAnswerThird.setFont(font2)
        self.ledtAnswerThird.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.ledtAnswerThird, 8, 2, 1, 3)

        self.ledtAnswerFour = QLineEdit(self.pgCreate)
        self.ledtAnswerFour.setObjectName(u"ledtAnswerFour")
        self.ledtAnswerFour.setFont(font2)
        self.ledtAnswerFour.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.ledtAnswerFour, 9, 2, 1, 3)

        self.ptedQuestion = QPlainTextEdit(self.pgCreate)
        self.ptedQuestion.setObjectName(u"ptedQuestion")
        self.ptedQuestion.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.ptedQuestion.setFrameShape(QFrame.StyledPanel)

        self.gridLayout_5.addWidget(self.ptedQuestion, 2, 2, 2, 3)

        self.stackProfessor.addWidget(self.pgCreate)
        self.pgEdit = QWidget()
        self.pgEdit.setObjectName(u"pgEdit")
        self.stackProfessor.addWidget(self.pgEdit)

        self.verticalLayout_2.addWidget(self.stackProfessor)

        self.tabWidget.addTab(self.tbProfessor, "")
        self.btAbout = QWidget()
        self.btAbout.setObjectName(u"btAbout")
        self.verticalLayout_4 = QVBoxLayout(self.btAbout)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.textBrowser = QTextBrowser(self.btAbout)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_4.addWidget(self.textBrowser)

        self.label = QLabel(self.btAbout)
        self.label.setObjectName(u"label")
        self.label.setEnabled(False)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label)

        self.tabWidget.addTab(self.btAbout, "")

        self.verticalLayout_7.addWidget(self.tabWidget)

        self.stackApp.addWidget(self.pgApp)

        self.horizontalLayout.addWidget(self.stackApp)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackApp.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.stckStudent.setCurrentIndex(0)
        self.stackProfessor.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnStartApp.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0410\u0427\u0410\u0422\u042c \u0418\u0421\u041f\u041e\u041b\u042c\u0417\u041e\u0412\u0410\u041d\u0418\u0415 \u041f\u0420\u0418\u041b\u041e\u0416\u0415\u041d\u0418\u042f", None))
        self.tbrSummaryApp.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:16pt; font-weight:700; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0414\u043e\u0431\u0440\u043e \u043f\u043e\u0436\u0430\u043b\u043e\u0432\u0430\u0442\u044c \u0432 \u044d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u043e\u0435 \u0443\u0447\u0435\u0431\u043d\u043e\u0435 \u043f\u043e\u0441\u043e\u0431\u0438\u0435 \u043f\u043e \u0442\u0435\u043c\u0435 &quot;\u041f\u043e\u0434\u0434\u0435\u0440\u0436\u043a\u0430 \u0438 \u0442\u0435\u0441\u0442\u0438"
                        "\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043d\u044b\u0445 \u043c\u043e\u0434\u0443\u043b\u0435\u0439&quot;!</p></body></html>", None))
        self.btnShowExample.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0420\u0410\u041a\u0422\u0418\u041a\u0410", None))
        self.btnShowMethodist.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0415\u0422\u041e\u0414\u0418\u0427\u0415\u0421\u041a\u0418\u0415 \u041c\u0410\u0422\u0415\u0420\u0418\u0410\u041b\u042b", None))
        self.btnShowTutorial.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0415\u041e\u0420\u0418\u042f", None))
        self.btnTest.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0415\u0421\u0422", None))
        self.btnGoToStartState.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0415\u0420\u041d\u0423\u0422\u042c\u0421\u042f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tbStudent), QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0443\u0434\u0435\u043d\u0442\u0443", None))
        self.btnLogin.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0412\u0422\u041e\u0420\u0418\u0417\u0410\u0426\u0418\u042f", None))
        self.gboxFileWorkers.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0410\u0419\u041b\u042b", None))
        self.btnAddTutorial.setText(QCoreApplication.translate("MainWindow", u"\u0414\u041e\u0411\u0410\u0412\u0418\u0422\u042c \u0422\u0415\u041e\u0420\u0418\u042e", None))
        self.btnDelTutorial.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0414\u0410\u041b\u0418\u0422\u042c \u0422\u0415\u041e\u0420\u0418\u042e", None))
        self.btnAddExample.setText(QCoreApplication.translate("MainWindow", u"\u0414\u041e\u0411\u0410\u0412\u0418\u0422\u042c \u041f\u0420\u0410\u041a\u0422\u0418\u041a\u0423", None))
        self.btnDelExample.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0414\u0410\u041b\u0418\u0422\u042c \u041f\u0420\u0410\u041a\u0422\u0418\u041a\u0423", None))
        self.btnDelTest.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0414\u0410\u041b\u0418\u0422\u042c \u0422\u0415\u0421\u0422", None))
        self.btnAddMethodist.setText(QCoreApplication.translate("MainWindow", u"\u0414\u041e\u0411\u0410\u0412\u0418\u0422\u042c \u041c\u0415\u0422\u041e\u0414\u0418\u0427\u0415\u0421\u041a\u0418\u0415 \u041c\u0410\u0422\u0415\u0420\u0418\u0410\u041b\u042b", None))
        self.btnDelMethodist.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0414\u0410\u041b\u0418\u0422\u042c \u041c\u0415\u0422\u041e\u041b\u0418\u0427\u0415\u0421\u041a\u0418\u0415 \u041c\u0410\u0422\u0415\u0420\u0418\u0410\u041b\u042b", None))
        self.btnAddQuestion.setText(QCoreApplication.translate("MainWindow", u"\u0414\u041e\u0411\u0410\u0412\u0418\u0422\u042c \u0412\u041e\u041f\u0420\u041e\u0421", None))
        self.btnEndCreateTest.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0410\u041a\u041e\u041d\u0427\u0418\u0422\u042c \u0422\u0415\u0421\u0422", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u0415\u0420\u041d\u042b\u0419 \u041e\u0422\u0412\u0415\u0422", None))
        self.rbtnAnswerFirst.setText("")
        self.rbtnAnswerSecond.setText("")
        self.rbtnAnswerThird.setText("")
        self.rbtnAnswerFour.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tbProfessor), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u0442\u0435\u043b\u044e", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:'Times New Roman,serif'; font-size:14pt; color:#000000;\">\u041e\u0431\u0449\u0438\u0435 \u0441\u0432\u0435\u0434\u0435\u043d\u0438\u044f</span><span style=\" font-family:'MS Shell Dlg 2';\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span st"
                        "yle=\" font-family:'Times New Roman,serif'; font-size:14pt; color:#000000;\">\u042d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u043e\u0435 \u0443\u0447\u0435\u0431\u043d\u043e\u0435 \u043f\u043e\u0441\u043e\u0431\u0438\u0435 \u00ab\u041f\u043e\u0434\u0434\u0435\u0440\u0436\u043a\u0430 \u0438 \u0442\u0435\u0441\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043d\u044b\u0445 \u043c\u043e\u0434\u0443\u043b\u0435\u0439\u00bb - \u044d\u0442\u043e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043d\u043e\u0435 \u043e\u0431\u0435\u0441\u043f\u0435\u0447\u0435\u043d\u0438\u0435, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u043c \u0438\u0437\u043b\u0430\u0433\u0430\u0435\u0442\u0441\u044f \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b \u0432 \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u043d\u043e\u0439 \u043e\u0431\u043b\u0430\u0441\u0442\u0438 \u0437\u043d\u0430\u043d\u0438\u0439. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0p"
                        "x; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:'Times New Roman,serif'; font-size:14pt; color:#000000;\">\u0412 \u0434\u0430\u043d\u043d\u043e\u043c \u0443\u0447\u0435\u0431\u043d\u043e\u043c \u043f\u043e\u0441\u043e\u0431\u0438\u0438 \u0432\u044b \u043d\u0430\u0439\u0434\u0435\u0442\u0435 \u0442\u0435\u043e\u0440\u0435\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0438 \u043f\u0440\u0430\u043a\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u044b, \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u043f\u043e\u043c\u043e\u0433\u0443\u0442 \u0432\u0430\u043c \u0443\u043b\u0443\u0447\u0448\u0438\u0442\u044c \u0441\u0432\u043e\u0438 \u0437\u043d\u0430\u043d\u0438\u044f \u0438 \u043d\u0430\u0432\u044b\u043a\u0438 \u0432 \u043e\u0431\u043b\u0430\u0441\u0442\u0438 \u043f\u043e\u0434\u0434\u0435\u0440\u0436\u043a\u0438 \u0438 \u0442\u0435\u0441\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f"
                        " \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043d\u044b\u0445 \u043c\u043e\u0434\u0443\u043b\u0435\u0439. \u041a\u0440\u043e\u043c\u0435 \u0442\u043e\u0433\u043e, \u0432\u044b \u0441\u043c\u043e\u0436\u0435\u0442\u0435 \u043f\u0440\u043e\u0439\u0442\u0438 \u0442\u0435\u0441\u0442\u044b \u0438 \u043e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u0438\u0445 \u043d\u0430 \u043f\u043e\u0447\u0442\u0443 \u0432\u0430\u0448\u0435\u0433\u043e \u043f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u0442\u0435\u043b\u044f \u0434\u043b\u044f \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0438.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:'Times New Roman,serif'; font-size:14pt; color:#000000;\">\u0422\u0435\u043e\u0440\u0435\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u044b</span></p>\n"
"<p style=\" margin-top:12px; margin-bot"
                        "tom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:'Times New Roman,serif'; font-size:14pt; color:#000000;\">\u0412 \u043d\u0430\u0448\u0435\u043c \u0443\u0447\u0435\u0431\u043d\u043e\u043c \u043f\u043e\u0441\u043e\u0431\u0438\u0438 \u0432\u044b \u043d\u0430\u0439\u0434\u0435\u0442\u0435 \u043c\u043d\u043e\u0436\u0435\u0441\u0442\u0432\u043e \u0442\u0435\u043e\u0440\u0435\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0445 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u043e\u0432, \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u043f\u043e\u0437\u0432\u043e\u043b\u044f\u0442 \u0432\u0430\u043c \u0443\u0433\u043b\u0443\u0431\u0438\u0442\u044c\u0441\u044f \u0432 \u0442\u0435\u043c\u0443 \u043f\u043e\u0434\u0434\u0435\u0440\u0436\u043a\u0438 \u0438 \u0442\u0435\u0441\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043d\u044b\u0445 \u043c\u043e\u0434\u0443\u043b\u0435\u0439. \u0412\u044b "
                        "\u0441\u043c\u043e\u0436\u0435\u0442\u0435 \u043e\u0437\u043d\u0430\u043a\u043e\u043c\u0438\u0442\u044c\u0441\u044f \u0441 \u0442\u0435\u043e\u0440\u0438\u0435\u0439 \u0438 \u0438\u0437\u0443\u0447\u0438\u0442\u044c \u043e\u0441\u043d\u043e\u0432\u043d\u044b\u0435 \u0442\u0435\u0440\u043c\u0438\u043d\u044b \u0438 \u043f\u043e\u043d\u044f\u0442\u0438\u044f, \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u0432\u0430\u043c \u043f\u043e\u043d\u0430\u0434\u043e\u0431\u044f\u0442\u0441\u044f \u0432 \u0440\u0430\u0431\u043e\u0442\u0435.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:'Times New Roman,serif'; font-size:14pt; color:#000000;\">\u041f\u0440\u0430\u043a\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u044b </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-"
                        "indent:0px; line-height:150%;\"><span style=\" font-family:'Times New Roman,serif'; font-size:14pt; color:#000000;\">\u041d\u0430\u0448\u0435 \u0443\u0447\u0435\u0431\u043d\u043e\u0435 \u043f\u043e\u0441\u043e\u0431\u0438\u0435 \u0442\u0430\u043a\u0436\u0435 \u0441\u043e\u0434\u0435\u0440\u0436\u0438\u0442 \u043c\u043d\u043e\u0436\u0435\u0441\u0442\u0432\u043e \u043f\u0440\u0430\u043a\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0445 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u043e\u0432, \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u043f\u043e\u043c\u043e\u0433\u0443\u0442 \u0432\u0430\u043c \u043f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u043e\u043b\u0443\u0447\u0435\u043d\u043d\u044b\u0435 \u0437\u043d\u0430\u043d\u0438\u044f \u043d\u0430 \u043f\u0440\u0430\u043a\u0442\u0438\u043a\u0435. \u0412\u044b \u0441\u043c\u043e\u0436\u0435\u0442\u0435 \u043e\u0437\u043d\u0430\u043a\u043e\u043c\u0438\u0442\u044c\u0441\u044f \u0441 \u0440\u0430\u0437\u043b\u0438\u0447\u043d\u044b\u043c\u0438 \u0438\u043d"
                        "\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442\u0430\u043c\u0438, \u043c\u0435\u0442\u043e\u0434\u0430\u043c\u0438 \u0438 \u0441\u0442\u0440\u0430\u0442\u0435\u0433\u0438\u044f\u043c\u0438, \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u0432\u044b \u043c\u043e\u0436\u0435\u0442\u0435 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c \u043f\u0440\u0438 \u0440\u0430\u0431\u043e\u0442\u0435 \u0441 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043d\u044b\u043c\u0438 \u043c\u043e\u0434\u0443\u043b\u044f\u043c\u0438.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:'Times New Roman,serif'; font-size:14pt; color:#000000;\">\u0422\u0435\u0441\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\""
                        " font-family:'Times New Roman,serif'; font-size:14pt; color:#000000;\">\u0411\u044b\u043b\u043e \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0430\u043d\u043e \u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u043e \u0442\u0435\u0441\u0442\u043e\u0432, \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u043f\u043e\u043c\u043e\u0433\u0443\u0442 \u0432\u0430\u043c \u043f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c \u0441\u0432\u043e\u0438 \u0437\u043d\u0430\u043d\u0438\u044f \u0438 \u043f\u043e\u0434\u0433\u043e\u0442\u043e\u0432\u0438\u0442\u044c\u0441\u044f \u043a \u044d\u043a\u0437\u0430\u043c\u0435\u043d\u0443. \u041a\u0440\u043e\u043c\u0435 \u0442\u043e\u0433\u043e, \u043f\u043e\u0441\u043b\u0435 \u043f\u0440\u043e\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u044f \u0442\u0435\u0441\u0442\u043e\u0432 \u0432\u044b \u0441\u043c\u043e\u0436\u0435\u0442\u0435 \u043e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u0438\u0445 \u043d\u0430 \u043f\u043e\u0447\u0442\u0443 \u0432\u0430\u0448\u0435\u0433\u043e \u043f\u0440"
                        "\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u0442\u0435\u043b\u044f \u0434\u043b\u044f \u043e\u0446\u0435\u043d\u043a\u0438.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:'Times New Roman,serif'; font-size:14pt; color:#000000;\">\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u0430 \u043e\u0441\u0443\u0449\u0435\u0441\u0442\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u043f\u0440\u0438 \u043f\u043e\u043c\u043e\u0449\u0438 \u0432\u043a\u043b\u0430\u0434\u043e\u043a \u00ab\u0422\u0435\u043e\u0440\u0438\u044f\u00bb \u0438 \u00ab\u041f\u0440\u0430\u043a\u0442\u0438\u043a\u0430\u00bb, \u043f\u0440\u0438 \u043e\u0442\u043a\u0440\u044b\u0442\u0438\u0438 \u043b\u044e\u0431\u043e\u0439 \u0438\u0437 \u0432\u043a\u043b\u0430\u0434\u043e\u043a \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0435\u0442\u0441\u044f \u043e\u043a\u043d\u043e \u0441"
                        " \u043a\u043d\u043e\u043f\u043a\u0430\u043c\u0438 \u043f\u0440\u0438 \u043f\u043e\u043c\u043e\u0449\u0438 \u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u043e\u0441\u0443\u0449\u0435\u0441\u0442\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u043f\u0435\u0440\u0435\u0445\u043e\u0434 \u043f\u043e \u0433\u043b\u0430\u0432\u0430\u043c, \u0441\u043f\u0440\u0430\u0432\u0430 \u043e\u0442 \u043a\u043d\u043e\u043f\u043e\u043a \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u043b\u0435\u043d \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b, \u0442\u0430\u043a\u0436\u0435 \u0432\u043e \u0432\u043a\u043b\u0430\u0434\u043a\u0435 \u00ab\u041f\u0440\u0430\u043a\u0442\u0438\u043a\u0430\u00bb \u043f\u0440\u0438 \u043f\u043e\u043c\u043e\u0449\u0438 \u043a\u043d\u043e\u043f\u043a\u0438 \u00ab\u041f\u0435\u0440\u0435\u0439\u0442\u0438 \u043a \u0442\u0435\u0441\u0442\u0443\u00bb \u043e\u0441\u0443\u0449\u0435\u0441\u0442\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u043f\u0435\u0440\u0435\u0445\u043e\u0434 \u043a \u043f\u0440\u043e\u0445"
                        "\u043e\u0436\u0434\u0435\u043d\u0438\u044e \u0442\u0435\u0441\u0442\u043e\u0432.</span><span style=\" font-family:'MS Shell Dlg 2';\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:'Times New Roman,serif'; font-size:14pt; color:#000000;\">\u041f\u0440\u0438 \u043f\u043e\u043c\u043e\u0449\u0438 \u043a\u043d\u043e\u043f\u043e\u043a \u043d\u0430\u0432\u0438\u0433\u0430\u0446\u0438\u0438 \u0432 \u043f\u0440\u0430\u0432\u043e\u043c \u0432\u0435\u0440\u0445\u043d\u0435\u043c \u0443\u0433\u043b\u0443 \u043f\u043e\u0441\u043e\u0431\u0438\u0435 \u043c\u043e\u0436\u043d\u043e \u0441\u0432\u0435\u0440\u043d\u0443\u0442\u044c/\u0440\u0430\u0437\u0432\u0435\u0440\u043d\u0443\u0442\u044c \u043d\u0430 \u0432\u0435\u0441\u044c \u044d\u043a\u0440\u0430\u043d/\u0437\u0430\u043a\u0440\u044b\u0442\u044c</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:"
                        "0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:'Times New Roman,serif'; font-size:14pt; color:#000000;\">\u041d\u0430\u0434\u0435\u0435\u043c\u0441\u044f, \u0447\u0442\u043e \u043d\u0430\u0448\u0435 \u0443\u0447\u0435\u0431\u043d\u043e\u0435 \u043f\u043e\u0441\u043e\u0431\u0438\u0435 \u043f\u043e\u043c\u043e\u0436\u0435\u0442 \u0432\u0430\u043c \u0443\u043b\u0443\u0447\u0448\u0438\u0442\u044c \u0441\u0432\u043e\u0438 \u0437\u043d\u0430\u043d\u0438\u044f \u0438 \u043d\u0430\u0432\u044b\u043a\u0438 \u0432 \u043e\u0431\u043b\u0430\u0441\u0442\u0438 \u043f\u043e\u0434\u0434\u0435\u0440\u0436\u043a\u0438 \u0438 \u0442\u0435\u0441\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043d\u044b\u0445 \u043c\u043e\u0434\u0443\u043b\u0435\u0439. \u0415\u0441\u043b\u0438 \u0443 \u0432\u0430\u0441 \u0432\u043e\u0437\u043d\u0438\u043a\u043b\u0438 \u0432\u043e\u043f\u0440\u043e\u0441\u044b, \u043f\u043e\u0436\u0430\u043b\u0443\u0439"
                        "\u0441\u0442\u0430, \u043e\u0431\u0440\u0430\u0449\u0430\u0439\u0442\u0435\u0441\u044c \u043a \u0441\u0432\u043e\u0435\u043c\u0443 \u043f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u0442\u0435\u043b\u044e. \u0423\u0434\u0430\u0447\u0438 \u0432 \u0443\u0447\u0435\u0431\u0435!</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:'Times New Roman,serif'; font-size:14pt; color:#000000;\">\u00a0</span><span style=\" font-family:'MS Shell Dlg 2';\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:'Times New Roman,serif'; font-size:14pt; color:#000000;\">\u00a0</span><span style=\" font-family:'MS Shell Dlg 2';\"> </span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0430\u043d\u043e \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u043e\u043c \u0433\u0440\u0443\u043f\u043f\u044b 403 \u0418\u0421\u041f \u0411\u0430\u0440\u0430\u043a\u043e\u0432\u0441\u043a\u0438\u043c \u0414\u0430\u043d\u0438\u0438\u043b\u043e\u043c \u0414\u043c\u0438\u0442\u0440\u0438\u0435\u0432\u0438\u0447\u0435\u043c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.btAbout), QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
    # retranslateUi


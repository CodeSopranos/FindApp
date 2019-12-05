from PyQt5.QtWidgets import (QMainWindow,QWidget, QLabel, QLineEdit,  QPushButton,
                             QApplication, QMessageBox,QAction,QGridLayout,
                             QTableWidget, QTableWidgetItem,QInputDialog)
from PyQt5.QtCore import Qt,QCoreApplication,QRect, QTimer
from PyQt5.QtGui import QPainter, QColor, QFont,QIcon
from PyQt5.Qt import QVBoxLayout

import sys
import os
import importlib
import time

from FindApp import TableLayout
from FindApp import TextGetter
importlib.reload(TableLayout)
importlib.reload(TextGetter)

"""change fir to work project"""
path='C:\\Users\\Greg\\Google Диск\\ПМИ\\курсы\\базы данных\\проект\\git'
os.chdir(path)


class FindApp(QMainWindow):

    """

    class FindApp main layout of application

    """

    def __init__(self):
        super().__init__()

        TG=TextGetter.TextGetter()
        self.textAbout=TG.get_textAbout()
        self.AboutCounter=1
        self.timer_itr=0
        self.initUI()

    def initUI(self):

        """

        @method initUI creating main layput of application

        """

        self.setWindowTitle('FindApp')
        self.setWindowIcon(QIcon('image/logo.png'))


        """setting the about text"""
        self.label_result = QLabel('',self)
        self.label_result.setText(self.textAbout[0])
        self.label_result.resize(700, 400)
        self.label_result.move(0, 10)
        self.label_result.setAlignment(Qt.AlignCenter)
        self.label_result.setWordWrap(True)
        font = QFont("Ubuntu Mono", 16)
        self.label_result.setFont(font)

        """text timer"""
        self.timer = QTimer()
        self.timer.timeout.connect(self.tick)

        layout = QVBoxLayout()
        layout.addWidget(self.label_result)
        self.setLayout(layout)


        """QUIT toolbar botton"""
        exitAction = QAction(QIcon('image/quit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        """View DB toolbar botton"""
        viewDBAction = QAction(QIcon('image/database.png'), 'View Database', self)
        viewDBAction.setShortcut('Ctrl+T')
        viewDBAction.setStatusTip('View Database')
        viewDBAction.triggered.connect(self.viewDBBtn)

        """Find Rebel toolbar botton"""
        findAction = QAction(QIcon('image/find.png'), 'View Database', self)
        findAction.setShortcut('Ctrl+F')
        findAction.setStatusTip('Find Rebel')
        findAction.triggered.connect(self.findAction)

        """INFO toolbar botton"""
        infoAction = QAction(QIcon('image/info.png'), 'About', self)
        infoAction.setShortcut('Ctrl+I')
        infoAction.setStatusTip('About')
        infoAction.triggered.connect(self.infoActionBtn)

        """Set status bar """
        self.statusBar()

        """Set menubar"""
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        fileMenu.addAction(viewDBAction)

        """Set toolbar bottons"""
        toolbar = self.addToolBar('Find Rebel')
        toolbar.addAction(findAction)

        toolbar = self.addToolBar('View DB')
        toolbar.addAction(viewDBAction)

        toolbar = self.addToolBar('About')
        toolbar.addAction(infoAction)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)

        self.setGeometry(400, 100, 700, 450)
        self.show()

    def viewDBBtn(self):
        reply = QMessageBox.question(self, 'View DB',
            "Желаете посмотреть базу митингующих?", QMessageBox.Yes |
             QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.close()
            QWidget.__init__(self)
            TableLayout.initUI(self)
        else:
            event.ignore()

    """ launching timer for the about text"""
    def infoActionBtn(self,event):
        self.AboutCounter += 1
        self.label_result.setText(self.textAbout[self.AboutCounter])
        self.timer.start(2600)

    """timer text trigger"""
    def tick(self):
        if self.AboutCounter == len(self.textAbout)-1:
            self.label_result.setText(self.textAbout[self.AboutCounter])
            self.AboutCounter = 1
            self.timer.stop()
        else:
            self.AboutCounter += 1
            self.label_result.setText(self.textAbout[self.AboutCounter])



    def findAction(self,event):
        text, ok = QInputDialog.getText(self, 'Find Rebel',
            'Введите фамилию:')


    def backBtnAction(self):
        self.close()
        QWidget.__init__(self)
        self.initUI()

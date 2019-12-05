from PyQt5.QtWidgets import (QMainWindow,QWidget, QLabel, QLineEdit,  QPushButton,
                             QApplication, QMessageBox,QAction,QGridLayout,
                             QTableWidget, QTableWidgetItem,QInputDialog)
from PyQt5.QtCore import Qt,QCoreApplication,QRect
from PyQt5.QtGui import QPainter, QColor, QFont,QIcon
import sys


import importlib
from FindApp import TableLayout
from FindApp import TextGetter
importlib.reload(TableLayout)
importlib.reload(TextGetter)



class FindApp(QMainWindow):

    """
    class FindApp main layout of application
    """

    def __init__(self):
        super().__init__()

        TG=TextGetter.TextGetter()
        self.textAbout=TG.get_textAbout()
        self.AboutCounter=1
        self.initUI()

    def initUI(self):

        """
        @method initUI creating main layput of application
        """

        self.setWindowTitle('FindApp')
        self.setWindowIcon(QIcon('logo.png'))

        """QUIT toolbar botton"""
        exitAction = QAction(QIcon('quit_logo.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        """View DB toolbar botton"""
        viewDBAction = QAction(QIcon('logo.png'), 'View Database', self)
        viewDBAction.setShortcut('Ctrl+T')
        viewDBAction.setStatusTip('View Database')
        viewDBAction.triggered.connect(self.viewDBBtn)

        """Find Rebel toolbar botton"""
        findAction = QAction(QIcon('find.png'), 'View Database', self)
        findAction.setShortcut('Ctrl+F')
        findAction.setStatusTip('Find Rebel')
        findAction.triggered.connect(self.findAction)

        """INFO toolbar botton"""
        infoAction = QAction(QIcon('info.png'), 'About', self)
        infoAction.setShortcut('Ctrl+I')
        infoAction.setStatusTip('About')
        infoAction.triggered.connect(self.infoActionBtn)

        """Set menubar and toolbar """
        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        fileMenu.addAction(viewDBAction)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)

        toolbar = self.addToolBar('View DB')
        toolbar.addAction(viewDBAction)

        toolbar = self.addToolBar('Find Rebel')
        toolbar.addAction(findAction)

        toolbar = self.addToolBar('About')
        toolbar.addAction(infoAction)

        self.setGeometry(400, 100, 600, 400)
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


    def infoActionBtn(self,event):
        self.AboutCounter+=1
        reply = QMessageBox.question(self, 'About',
            "У Вас есть выбор?", QMessageBox.Yes |
             QMessageBox.Yes, QMessageBox.Yes)

    def findAction(self,event):
        text, ok = QInputDialog.getText(self, 'Find Rebel',
            'Введите фамилию:')


    def backBtnAction(self):
        self.close()
        QWidget.__init__(self)
        self.initUI()

    """draw textAbout"""
    def paintEvent(self,event):
        qp = QPainter()
        qp.begin(self)
        self.drawText(qp,event)
        qp.end()

    def drawText(self,qp,event):
        qp.setPen(QColor(0, 0, 0))
        qp.setFont(QFont('Decorative', 14))
        if self.AboutCounter<len(self.textAbout)+1:
            qp.drawText(event.rect(), Qt.AlignCenter, self.textAbout[self.AboutCounter-1])
        else:
            qp.drawText(event.rect(), Qt.AlignCenter, '...')

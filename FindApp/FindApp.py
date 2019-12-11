from PyQt5.QtWidgets import (QMainWindow,QWidget, QLabel, QLineEdit,  QPushButton,
                             QApplication, QMessageBox,QAction,QGridLayout,
                             QTableWidget, QTableWidgetItem,QInputDialog,
                             QDesktopWidget,QCompleter,QDialog,QDialogButtonBox)
from PyQt5.QtCore import Qt,QCoreApplication,QRect, QTimer ,QSize
from PyQt5.QtGui import QPainter, QColor, QFont,QIcon
from PyQt5.Qt import QVBoxLayout, QFormLayout

import sys
import os
import importlib
import time

from FindApp import TableLayout
from FindApp import TextGetter
from FindApp import DataGetter
from FindApp import FormLayout
importlib.reload(TableLayout)
importlib.reload(TextGetter)
importlib.reload(DataGetter)
importlib.reload(FormLayout)

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
        self.timerFlag=True
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

        """Find Rebel toolbar botton"""
        findAction = QAction(QIcon('image/find.png'), 'Find Rebel', self)
        findAction.setShortcut('Ctrl+F')
        findAction.setStatusTip('Find Rebel')
        findAction.triggered.connect(self.findActionBtn)

        """View DB toolbar botton"""
        viewDBAction = QAction(QIcon('image/database.png'), 'View Database', self)
        viewDBAction.setShortcut('Ctrl+V')
        viewDBAction.setStatusTip('View Database')
        viewDBAction.triggered.connect(self.viewDBBtn)

        """INFO toolbar botton"""
        infoAction = QAction(QIcon('image/info.png'), 'About', self)
        infoAction.setShortcut('Ctrl+I')
        infoAction.setStatusTip('About')
        infoAction.triggered.connect(self.infoActionBtn)

        """HIDE toolbar botton"""
        hideAction = QAction(QIcon('image/hide.png'), 'Hide toolbar', self)
        hideAction.setShortcut('Ctrl+H')
        hideAction.setStatusTip('Hide')
        hideAction.triggered.connect(self.hideTbAction)

        """ADD toolbar botton"""
        insertAction = QAction(QIcon('image/add.png'), 'Add a rebel', self)
        insertAction.setShortcut('Ctrl+A')
        insertAction.setStatusTip('Add a rebel')
        insertAction.triggered.connect(self.insertAction)

        """REMOVE toolbar botton"""
        removeAction = QAction(QIcon('image/remove.png'), 'Remove rebel', self)
        removeAction.setShortcut('Ctrl+R')
        removeAction.setStatusTip('Remove rebel')
        removeAction.triggered.connect(self.removeRebelAction)

        """CLEАR toolbar botton"""
        clearAction = QAction(QIcon('image/clear.png'), 'clear tables', self)
        clearAction.setShortcut('Ctrl+R')
        clearAction.setStatusTip('clear tables')
        clearAction.triggered.connect(self.clearAction)

        """SWITCH toolbar botton"""
        switchAction = QAction(QIcon('image/switcher.png'), 'Switch DB', self)
        switchAction.setShortcut('Ctrl+S')
        switchAction.setStatusTip('Switch DB')
        # switchAction.triggered.connect(self.removeRebelAction)

        """SHOW toolbar botton"""
        showAction = QAction(QIcon('image/show.png'), 'Show toolbar', self)
        showAction.setShortcut('Ctrl+S')
        showAction.setStatusTip('Show TB')
        showAction.triggered.connect(self.showTbAction)

        """QUIT toolbar botton"""
        exitAction = QAction(QIcon('image/quit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)


        """Set status bar """
        self.statusBar()

        """Set menubar"""
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(findAction)
        fileMenu.addAction(viewDBAction)
        fileMenu.addAction(infoAction)
        fileMenu.addAction(showAction)
        fileMenu.addAction(exitAction)


        """Set toolbar bottons"""
        self.toolbar = self.addToolBar('main')

        self.toolbar.addAction(hideAction)
        self.toolbar.addAction(findAction)
        self.toolbar.addAction(viewDBAction)
        self.toolbar.addAction(insertAction)
        self.toolbar.addAction(removeAction)
        self.toolbar.addAction(clearAction)
        self.toolbar.addAction(switchAction)
        self.toolbar.addAction(infoAction)
        self.toolbar.addAction(exitAction)

        self.toolbar.setToolButtonStyle( Qt.ToolButtonTextUnderIcon)
        self.toolbar.setIconSize(QSize(40, 40))


        """text edit line for rebel search by name """
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setPlaceholderText('Golunov...')
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit.resize(250,30)
        self.lineEdit.setFont(QFont("Arial",14))
        self.lineEdit.move(210,240)
        self.lineEdit.setHidden(True)

        """the first creating DB """
        DG=DataGetter.DataGetter(dbname='postgres')
        DG.createDB('nn')

        """filling crated DB"""
        DG=DataGetter.DataGetter(dbname='nn')
        DG.executeScript('procedures.sql')
        DG.createTables()
        DG.fillTables()
        DG.executeScript('views.sql')


        """auto completer for edit line using @DataGetter"""
        names,feature = DG.executeQuery('select * from v_childNames;')
        names=[item[0] for item in names]
        names=list(set(names))
        completer = QCompleter(names, self.lineEdit)
        self.lineEdit.setCompleter(completer)

        self.findBtn = QPushButton('Find',self)
        self.findBtn.setToolTip('Найдите этих ... найдите родителей этих...')
        self.findBtn.move(280,330)
        self.findBtn.setHidden(True)
        self.findBtn.clicked.connect(self.lineEditAction)

        self.setGeometry(300,100,700, 450)
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
        if self.timerFlag:
            self.AboutCounter += 1
            self.label_result.setText(self.textAbout[self.AboutCounter])
            self.timer.start(2800)

    """timer text trigger"""
    def tick(self):
        if self.AboutCounter == len(self.textAbout)-2:
            self. lineEdit.setHidden(False)
            self.findBtn.setHidden(False)


        if self.AboutCounter == len(self.textAbout)-1:
            self.label_result.setText(self.textAbout[self.AboutCounter])
            self.timerFlag=False
            self.timer.stop()
        else:
            self.AboutCounter += 1
            self.label_result.setText(self.textAbout[self.AboutCounter])



    def findActionBtn(self,event):
        text, ok = QInputDialog.getText(self, 'Find Rebel',
            'Введите имя:')
        self.getRebel(text)

    def lineEditAction(self,event):
        text = self.lineEdit.text()
        self.getRebel(text)

    def getRebel(self,name):
        DG=DataGetter.DataGetter(dbname='nn')
        if len(name) == 0:
            response = QMessageBox.question(self,'!!!!','<font size="14">Empty string!</font>', QMessageBox.Ok)
            return
        id_lst,feature = DG.findRebelQuery(name)
        id_lst=[item[0] for item in id_lst]
        if None in id_lst:
            id_lst.remove(None)
        if len(id_lst) == 0:
            response = QMessageBox.question(self,
                         'Good news','<font size="14">Резуальтат по запросу <i>' + name + '</i> не найден</font>',
                          QMessageBox.Ok)
            return
        print(id_lst,feature)
        if len(id_lst)>0:
            for id in id_lst:
                info_str,feature=DG.getRebelDataByID(id)
                info_str=info_str[0][0].split(' | ')
                print(info_str,feature)
                output_str='<font size="26"> Name: '+str(info_str[0])
                output_str+='<br>Age: '+str(info_str[1])
                output_str+='<br>School: '+str(info_str[2])
                output_str+='<br>SchoolPlace: '+str(info_str[3])+'</font>'
                response = QMessageBox.question(self,'Info about '+name,output_str,QMessageBox.Ok)


    def hideTbAction(self,event):
        self.toolbar.setHidden(True)


    def insertAction(self,event):
        FormLayout.FormLayout(self)
        # FormLayout.initUI(self)

    def removeRebelAction(self,event):
        text, ok = QInputDialog.getText(self, 'Find Rebel',
            'Введите имя:')
        # self.getRebel(text)

    def clearAction(self,event):
        reply = QMessageBox.question(self,'clear','Хотите очистить все записи?',
                                            QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            DG=DataGetter.DataGetter(dbname='nn')
            DG.clearTables()
            reply = QMessageBox.question(self,'clear','Таблицы пусты!',QMessageBox.Ok)
        else:
            event.ignore()

    def showTbAction(self,event):
        self.toolbar.setHidden(False)

    def backBtnAction(self):
        self.close()
        QWidget.__init__(self)
        self.initUI()

    def onChangedAction(self,text):
        self.lbl.setText(text)
        self.lbl.setHidden(False)

    def accept(self):
        info_dct={'name':self.name.text()+' '+self.lastname.text(),
                  'age':self.age.text(),
                  'school':self.combo_school.currentText(),
                  'meeting':self.combo_meeting.currentText()}
        DG = DataGetter.DataGetter(dbname='nn')
        # TODO: insert into base
        print(info_dct)

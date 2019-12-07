from PyQt5.QtWidgets import (QMainWindow,QWidget, QLabel, QLineEdit,  QPushButton,
							 QApplication, QMessageBox,QAction,QGridLayout,
							 QTableWidget, QTableWidgetItem,QInputDialog,QDesktopWidget)
from PyQt5.QtCore import Qt,QCoreApplication,QRect, QTimer ,QSize
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
		findAction.triggered.connect(self.findAction)

		"""View DB toolbar botton"""
		viewDBAction = QAction(QIcon('image/database.png'), 'View Database', self)
		viewDBAction.setShortcut('Ctrl+T')
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

		self.toolbar.addAction(findAction)
		self.toolbar.addAction(viewDBAction)
		self.toolbar.addAction(infoAction)
		self.toolbar.addAction(hideAction)
		self.toolbar.addAction(exitAction)

		self.toolbar.setToolButtonStyle( Qt.ToolButtonTextUnderIcon)
		self.toolbar.setIconSize(QSize(40, 40))


		"""# TODO: """

		self.titleEdit = QLineEdit(self)
		self.titleEdit.setAlignment(Qt.AlignCenter)
		self.titleEdit.resize(250,30)
		self.titleEdit.setFont(QFont("Arial",14))
		self.titleEdit.move(210,240)
		self.titleEdit.setHidden(True)


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
			self.titleEdit.setHidden(False)
		if self.AboutCounter == len(self.textAbout)-1:
			self.label_result.setText(self.textAbout[self.AboutCounter])
			self.timerFlag=False
			self.timer.stop()

		else:
			self.AboutCounter += 1
			self.label_result.setText(self.textAbout[self.AboutCounter])



	def findAction(self,event):
		text, ok = QInputDialog.getText(self, 'Find Rebel',
			'Введите фамилию:')

	def hideTbAction(self,event):
		self.toolbar.setHidden(True)

	def showTbAction(self,event):
		self.toolbar.setHidden(False)

	def backBtnAction(self):
		self.close()
		QWidget.__init__(self)
		self.initUI()

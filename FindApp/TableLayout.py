from PyQt5.QtWidgets import (QMainWindow,QWidget, QLabel, QLineEdit,  QPushButton,
                             QApplication, QMessageBox,QAction,QGridLayout,
                             QTableWidget, QTableWidgetItem, QToolBar,QHeaderView  )
from PyQt5.QtCore import Qt,QCoreApplication,QRect,QSize
from PyQt5.QtGui import QPainter, QColor, QFont,QIcon

import sys
import importlib
import psycopg2

from FindApp import DataGetter
importlib.reload(DataGetter)

def initUI(self):

    """

	@function initUi creating Table Layout

	"""

    self.setWindowTitle('FindApp')
    self.setWindowIcon(QIcon('image/logo.png'))

    backAction = QAction(QIcon('image/back.png'), 'Назад', self)
    backAction.setShortcut('Ctrl+Z')
    backAction.setStatusTip('back')
    backAction.triggered.connect(self.backBtnAction)

    """setting status bar"""
    self.statusBar()

    """setting toolbar"""
    toolbar = QToolBar('main')
    self.addToolBar(Qt.RightToolBarArea,toolbar)
    toolbar.addAction(backAction)
    toolbar.setToolButtonStyle( Qt.ToolButtonTextUnderIcon)
    toolbar.setIconSize(QSize(40, 40))

    central_widget = QWidget(self)
    self.setCentralWidget(central_widget)

    grid_layout = QGridLayout()
    central_widget.setLayout(grid_layout)

    DG=DataGetter.DataGetter(dbname='nn')
    frame,features=DG.executeQuery('select * from v_full_info')

    table = QTableWidget(self)
    table.setColumnCount(len(frame[0]))
    table.setRowCount(len(frame))
    table.setHorizontalHeaderLabels(features)
    table.resizeColumnsToContents()

    for i in range(len(frame)):
        for j in range(len(frame[0])):
            table.setItem(i, j, QTableWidgetItem(str(frame[i][j])))

    grid_layout.addWidget(table, 0, 0)


    self.setGeometry(200, 100, 500, 400)
    header = table.horizontalHeader()
    for i in range(len(frame[0])):
        header.setSectionResizeMode(i, QHeaderView.ResizeToContents)
    header.setStretchLastSection(True)

    self.show()

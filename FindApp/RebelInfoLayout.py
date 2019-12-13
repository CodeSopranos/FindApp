from PyQt5.QtWidgets import (QMainWindow,QWidget, QLabel, QLineEdit,  QPushButton,
                             QApplication, QMessageBox,QAction,QGridLayout,
                             QTableWidget, QTableWidgetItem, QToolBar,QHeaderView, QAbstractScrollArea)
from PyQt5.QtCore import Qt,QCoreApplication,QRect,QSize
from PyQt5.QtGui import QPainter, QColor, QFont,QIcon

import sys
import importlib
import psycopg2

from FindApp import DataGetter
importlib.reload(DataGetter)

def initUI(self, info_str):
    """

    @function initUi creating Table Layout

    """
    self.setWindowTitle('FindApp')
    self.setWindowIcon(QIcon('image/logo.png'))

    """back toolbar botton"""
    backAction = QAction(QIcon('image/back.png'), 'Назад', self)
    backAction.setShortcut('Ctrl+Z')
    backAction.setStatusTip('back')
    backAction.triggered.connect(self.backAct)

    """update toolbar botton"""
    updateAction = QAction(QIcon('image/update.png'), 'Обновить', self)
    updateAction.setShortcut('Ctrl+U')
    updateAction.setStatusTip('update')
    updateAction.triggered.connect(self.updateBtnAction)

    """setting status bar"""
    self.statusBar()

    """setting toolbar"""
    toolbar = QToolBar('main')
    self.addToolBar(Qt.RightToolBarArea,toolbar)
    toolbar.addAction(backAction)
    toolbar.addAction(updateAction)
    toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
    toolbar.setIconSize(QSize(30, 30))

    central_widget = QWidget(self)
    self.setCentralWidget(central_widget)

    grid_layout = QGridLayout()
    central_widget.setLayout(grid_layout)

    table = QTableWidget(self)
    table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

    print(info_str)
    table.setColumnCount(4)
    table.setRowCount(1)
    table.setHorizontalHeaderLabels(['Name','Age','School','Meeting'])
    table.resizeColumnsToContents()

    table.setItem(0, 0, QTableWidgetItem(info_str[0]))
    table.setItem(0, 1, QTableWidgetItem(info_str[1]))
    table.setItem(0, 2, QTableWidgetItem(info_str[2]))
    table.setItem(0, 3, QTableWidgetItem(info_str[3]))

    font = QFont()
    font.setPointSize(16)
    table.setFont(font)
    grid_layout.addWidget(table, 0, 0)
    header = table.horizontalHeader()
    header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
    header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
    header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
    header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
    # header.setStretchLastSection(True)
    self.show()

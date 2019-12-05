from PyQt5.QtWidgets import (QMainWindow,QWidget, QLabel, QLineEdit,  QPushButton,
                             QApplication, QMessageBox,QAction,QGridLayout,
                             QTableWidget, QTableWidgetItem)
from PyQt5.QtCore import Qt,QCoreApplication,QRect
from PyQt5.QtGui import QPainter, QColor, QFont,QIcon

import sys

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

    self.statusBar()
    toolbar = self.addToolBar('Back')
    toolbar.addAction(backAction)


    central_widget = QWidget(self)
    self.setCentralWidget(central_widget)

    grid_layout = QGridLayout()
    central_widget.setLayout(grid_layout)

    table = QTableWidget(self)
    table.setColumnCount(5)
    table.setRowCount(10)
    table.setHorizontalHeaderLabels(['X1','X2','X3','X4','X5'])
    table.resizeColumnsToContents()

    grid_layout.addWidget(table, 0, 0)

    self.setGeometry(200, 100, 300, 500)
    self.show()

from PyQt5.QtWidgets import (QMainWindow,QWidget, QLabel, QLineEdit,  QPushButton,
                             QApplication, QMessageBox,QAction,QGridLayout,
                             QTableWidget, QTableWidgetItem, QToolBar,QHeaderView ,
                             QDialog,QFormLayout,QDialogButtonBox, QComboBox )
from PyQt5.QtCore import Qt,QCoreApplication,QRect,QSize, QRegExp
from PyQt5.QtGui import QPainter, QColor, QFont,QIcon,QRegExpValidator

import sys
import importlib
import psycopg2

from FindApp import DataGetter
importlib.reload(DataGetter)

class UpdateForm:

    """

    @class FormLayout insertion profile form layout

    """

    def __init__(self,main_window):
        main_window.update_form = QDialog()
        main_window.update_form.setWindowTitle('Update Rebel Info')
        main_window.update_form.setWindowIcon(QIcon('image/logo.png'))
        self.main_window = main_window
        self.initUI(main_window)

    def initUI(self,main_window):
        main_window.name = QLineEdit()
        main_window.lastname = QLineEdit()
        main_window.age = QLineEdit()

        """setting validators"""
        reg_ex = QRegExp("([A-Z][a-z]{20})|([А-Я][а-я]{20})")
        input_validator = QRegExpValidator(reg_ex, main_window.name)
        input_validator = QRegExpValidator(reg_ex, main_window.lastname)
        main_window.name.setValidator(input_validator)
        main_window.lastname.setValidator(input_validator)
        reg_ex = QRegExp("[1-9][0-9]")
        input_validator = QRegExpValidator(reg_ex, main_window.age)
        main_window.age.setValidator(input_validator)

        layout = QFormLayout()
        layout.addRow('Name:', main_window.name)
        layout.addRow('Lastname:', main_window.lastname)
        layout.addRow('Age:', main_window.age)

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(main_window.acceptUpdate)
        self.buttonBox.rejected.connect(main_window.update_form.reject)
        layout.addWidget(self.buttonBox)

        main_window.update_form.setLayout(layout)
        main_window.update_form.exec()

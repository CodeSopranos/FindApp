from PyQt5.QtWidgets import (QMainWindow,QWidget, QLabel, QLineEdit,  QPushButton,
                             QApplication, QMessageBox,QAction,QGridLayout,
                             QTableWidget, QTableWidgetItem, QToolBar,QHeaderView ,
                             QDialog,QFormLayout,QDialogButtonBox, QComboBox )
from PyQt5.QtCore import Qt,QCoreApplication,QRect,QSize
from PyQt5.QtGui import QPainter, QColor, QFont,QIcon

import sys
import importlib
import psycopg2

from FindApp import DataGetter
importlib.reload(DataGetter)

class FormLayout:
    def __init__(self,main_window):
        main_window.profile = QDialog(main_window)
        main_window.profile.setWindowTitle('New Rebel')
        self.main_window=main_window
        self.initUI(main_window)

    def initUI(self,main_window):
        main_window.name = QLineEdit()
        main_window.lastname = QLineEdit()
        main_window.age = QLineEdit()
        main_window.school = QLineEdit()
        main_window.schoolplace = QLineEdit()

        layout = QFormLayout()
        layout.addRow('Name:',main_window.name)
        layout.addRow('Lastname:',main_window.lastname)
        layout.addRow('Age:',main_window.age)

        DG = DataGetter.DataGetter(dbname='nn')
        frame,features=DG.executeQuery('select * from v_schoolNames')
        frame = [item[0] for item in frame]
        frame = list(set(frame))
        main_window.combo_school = QComboBox()
        main_window.combo_school.addItems(frame)
        layout.addRow('Choose school:',main_window.combo_school)

        frame,features=DG.executeQuery('select * from v_meetingNames')
        main_window.combo_meeting = QComboBox()
        frame=[item[0] for item in frame]
        frame = list(set(frame))
        main_window.combo_meeting.addItems(frame)
        layout.addRow('Choose meeting:',main_window.combo_meeting)

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(main_window.accept)
        self.buttonBox.rejected.connect(main_window.profile.reject)
        layout.addWidget(self.buttonBox)


        main_window.profile.setLayout(layout)
        main_window.profile.show()

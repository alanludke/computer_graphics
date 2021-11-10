import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *


class AddObject_GUI(QDialog):
    def __init__(self, parent):
        super(AddObject_GUI, self).__init__(parent)
        self.initUI()
        self.parent = parent

    def initUI(self):
        uic.loadUi("src/view/new_object_gui.ui", self)

        # buttons
        self.txt_coord.setPlaceholderText("(x0,y0,z0),(xn,yn,zn)")
        self.btn_add.clicked.connect(self.btn_add_clicked)

    def btn_add_clicked(self):
        self.parent.terminal_out.append("btn_add clicked!!!")
        print("btn_add clicked")

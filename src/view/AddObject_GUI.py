import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *

class AddObject_GUI(QDialog):
    def __init__(self):
        super(AddObject_GUI,self).__init__()
        self.initUI()

    def btn_add_object_clicked(self):
        print("btn_add_object_clicked clicked")
        
    def initUI(self):
        uic.loadUi("src/view/new_object_gui.ui", self)
        
        # buttons
        self.txt_coord.setPlaceholderText("(x0,y0,z0),(xn,yn,zn)")
        # self.btn_add_object.clicked.connect(self.btn_add_object_clicked)

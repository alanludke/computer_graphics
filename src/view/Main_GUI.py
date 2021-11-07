import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *

from src.view.AddObject_GUI import AddObject_GUI

class Main_GUI(QMainWindow):
    def __init__(self):
        super(Main_GUI,self).__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi("src/view/main_gui.ui", self)
        self.show()
    
        # buttons
        self.btn_add_object.clicked.connect(self.btn_add_object_clicked)
    
    def btn_add_object_clicked(self):
        self.terminal_out.append("btn_add_object_clicked clicked!!!")
        print("btn_add_object_clicked clicked")
        self.object_gui = AddObject_GUI()
        self.object_gui.window()

def window():
    app = QApplication(sys.argv)
    win = Main_GUI()
    win.show()
    sys.exit(app.exec_())
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *

class AddObject_GUI(QMainWindow):
    def __init__(self):
        super(AddObject_GUI,self).__init__()
        self.initUI()

    def btn_add_object_clicked(self):
        self.terminal_out.append("btn_add_object_clicked clicked!!!")
        print("btn_add_object_clicked clicked")
        
    def initUI(self):
        uic.loadUi("src/view/new_object_gui.ui", self)
        self.show()
        
        # buttons
        self.terminal_out.setPlaceholderText("Don't mind me.")
        self.btn_add_object.clicked.connect(self.btn_add_object_clicked)

def window():
    app = QApplication(sys.argv)
    win = AddObject_GUI()
    win.show()
    sys.exit(app.exec_())
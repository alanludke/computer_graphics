import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *

class Main_GUI(QMainWindow):
    def __init__(self):
        super(Main_GUI,self).__init__()
        self.initUI()

    def button_clicked(self):
	    print("clicked")

    def initUI(self):
        uic.loadUi("src/view/gui.ui", self)
        self.show()

        #buttons
        self.addObject.clicked.connect(self.button_clicked)

    def get_window(self):
        return self.window

def window():
    app = QApplication(sys.argv)
    win = Main_GUI()
    win.show()
    sys.exit(app.exec_())
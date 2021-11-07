import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *

from src.view.Main_GUI import Main_GUI
from src.view.AddObject_GUI import AddObject_GUI

class Controller():
    def __init__(self):
        self.app = QApplication(sys.argv)

        self.main_gui = Main_GUI()
        self.main_gui.window()

    # def callObjectScreen():
    #     object_screen.show()

    # def callPointScreen():
    #     point_screen.show()

    # def objectScreenEvents():
    #     object_screen.addPoint.clicked.connect(callPointScreen)
    def start(self):
        self.app.exec()
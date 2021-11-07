import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *

from src.view.Main_GUI import Main_GUI
from src.view.Object_GUI import Object_GUI

class Controller():
    def __init__(self):
        self.app = QApplication(sys.argv)

        self.main_gui = Main_GUI()
        self.main_gui.window()
        # self.main_gui.show()
        # self.main_gui.window()
        # main_gui.get_window.addObject.clicked.connect(print("lele"))
        

        # object_gui = Object_GUI()
        # object_gui.show()
        # # point_screen = uic.loadUi("src/view/NewPointScreen.ui")

        # windowEvents()
        # main_gui.add_object()
        # objectScreenEvents()
        # app.exec()

    # def callObjectScreen():
    #     object_screen.show()

    # def callPointScreen():
    #     point_screen.show()

    # def objectScreenEvents():
    #     object_screen.addPoint.clicked.connect(callPointScreen)

    def start(self):
        self.app.exec()
import sys
from PyQt5.QtWidgets import *

from src.view.Main_GUI import Main_GUI
from src.view.AddObject_GUI import AddObject_GUI

"""

"""


class Controller:
    def __init__(self):
        self.app = QApplication(sys.argv)

        self.main_gui = Main_GUI()
        self.main_gui.window()

    def start(self):
        self.app.exec()

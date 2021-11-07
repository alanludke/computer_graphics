import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *

class Object_GUI():
    def __init__(self):
        self.window = uic.loadUi("src/view/NewObjectScreen.ui")
    
    # def windowEvents(self):
    #     self.get_window().addObject.clicked.connect(callObjectScreen)

    def get_window(self):
        return self.window
    
    def show(self):
        self.window.show()
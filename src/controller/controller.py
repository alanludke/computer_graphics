from PyQt5 import QtWidgets, uic

class Controller():
    def __init__(self):
        app = QtWidgets.QApplication([])
        window = uic.loadUi("../view/gui.ui")
        window.show()
        app.exec()

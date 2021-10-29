import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *

class Gui(QMainWindow):
    def __init__(self):
        super().__init__()

        self.top = 100
        self.left = 200
        self.width = 1000
        self.height = 600
        self.title = "Computação Gráfica"
        menufunc = self.menuFuncoes()
        self.drawWindow()

    def menuFuncoes(self):
        layout = QVBoxLayout()
        frame = QFrame()
        frame.setMaximumWidth(100)
        frame.setLayout(layout)
        grupo = QGroupBox()
        grupo.setTitle("Menu de Funções")
        layout.addWidget(grupo)
        buttonUp = QPushButton("Up", self)
        buttonUp.resize(50,25)
        buttonUp.move(50, 100)
        buttonDown = QPushButton("Down", self)
        buttonDown.resize(50,25)
        buttonDown.move(50, 150)
        buttonRight = QPushButton("Right", self)
        buttonRight.resize(50,25)
        buttonRight.move(75, 125)
        buttonLeft = QPushButton("Left", self)
        buttonLeft.resize(50,25)
        buttonLeft.move(25, 125)
        buttonIn = QPushButton("In", self)
        buttonIn.resize(50,25)
        buttonIn.move(150, 100)
        buttonOut = QPushButton("Out", self)
        buttonOut.resize(50,25)
        buttonOut.move(150, 150)
        
    
    def drawWindow(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)
        self.show()


# app = QApplication(sys.argv)
# j = Gui()
# sys.exit(app.exec_())

app = QtWidgets.QApplication([])
window = uic.loadUi("gui.ui")
window.show()
app.exec()

import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QLine, QLineF, QRect

from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QLabel, QWidget

class Viewport(QLabel):
    def __init__(self):
        super().__init__()
        self.objects = []
        # self.setFixedWidth(500)
        # self.setFixedHeight(500)
        self.setStyleSheet("QLabel {background-color: rgb(239, 41, 41)}")
        # self.setAutoFillBackground(True)

        self.canvas = QtGui.QPixmap(500,500)
        self.setPixmap(self.canvas)
        # self.paintEvent()

        # painter = QPainter(self.pixmap())
        # pen = QPen()
        # pen.setWidth(5)
        # painter.setPen(pen)
        # painter.drawEllipse(300, 300, 150, 150)

        painter = QtGui.QPainter(self.pixmap())
        painter.drawLine(10, 10, 150, 100)
        painter.end()



    # def paintEvent(self, event):
    #     painter = QPainter(self.pixmap())
    #     painter.drawLine(10,10,300,200)
    #     painter.end()

    #     # pen = QPen()
    #     # pen.setWidth(5)

    #     painter = QPainter(self)
    #     # line = QLine(10,10,300,200)
    #     painter.drawPixmap(10,10,300,200, self.canvas)
    #     # painter.setPen(pen)
    #     # painter.drawEllipse(300, 300, 150, 150)

    
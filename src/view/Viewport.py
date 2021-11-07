import sys

from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QWidget

class Viewport(QWidget):
    def __init__(self):
        super().__init__()
        self.objects = []

    def paintEvent(self):
        pen = QPen()
        pen.setWidth(5)

        painter = QPainter(self)
        # painter.drawPixmap(self.rect())
        painter.setPen(pen)
        painter.drawEllipse(300, 300, 150, 150)

    
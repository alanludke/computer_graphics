from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QColor, QPainter, QPen
import numpy as np


class Point:
    def __init__(self, x, y, z):
        self.coordinates = [x, y, z]

    def get_x(self):
        return self.coordinates[0][0]

    def get_y(self):
        return self.coordinates[0][1]

    def get_z(self):
        return self.coordinates[0][2]

    def set_x(self, x):
        self.coordinates[0][0] = x

    def set_y(self, y):
        self.coordinates[0][1] = y

    def set_z(self, z):
        self.coordinates[0][2] = z

    def asnumpy(self):
        return self.coord

    def transform(self, t):
        if not isinstance(t, np.ndarray):
            self.coord = np.dot(self.coord, np.array(t))
        else:
            self.coord = np.dot(self.coord, t)

    def __str__(self) -> str:
        return f"({self.get_x()},{self.get_y()},{self.get_z()})"

    def to_QPointF(self) -> QPointF:
        return QPointF(self.get_x(), self.get_y())
        
    def draw(self, viewport):
        painter = QPainter(viewport)
        pen = QPen()

        pen.setWidth(50)
        pen.setColor(QColor(255, 255, 255))
        painter.setPen(pen)
        
        # painter.drawLine(self.origin.to_QPointF(), self.destiny.to_QPointF())
        painter.drawPoint(self.to_QPointF())
        painter.drawLine(self.to_QPointF(),self.to_QPointF())


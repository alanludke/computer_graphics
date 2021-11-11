from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QColor, QPainter, QPen
import numpy as np


class Point:
    def __init__(self, x, y, z):
        self.coordinates = [[x, y, z]]

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

    def viewport_transformation(self, viewport):
        v_point = viewport.viewport_transform(self)
        return v_point
    
    def draw(self, viewport):
        painter = QPainter(viewport)
        pen = QPen()

        pen.setWidth(2)
        pen.setColor(QColor(255, 0, 1))
        painter.setPen(pen)

        painter.drawPoint(self.to_QPointF())

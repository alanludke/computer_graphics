from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QColor, QPainter, QPen
import numpy as np


class Point:
    def __init__(self, name, x, y, z):
        self.coordinates = [[x, y, z]]
        self.name = name

    def getName(self):
        return self.name

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

    def __str__(self) -> str:
        return f"({self.get_x()},{self.get_y()},{self.get_z()})"

    # converte o objeto Point em um objeto QPointF do PyQt5
    def to_QPointF(self) -> QPointF:
        return QPointF(self.get_x(), self.get_y())

    # Transforma a coordenada do ponto em coordenada de viewport
    def viewport_transformation(self, viewport):
        v_point = viewport.viewport_transform(self)
        return v_point

    # Aplica a transformada de viewport nos pontos do objeto e depois desenha
    def draw(self, viewport):
        painter = QPainter(viewport)
        pen = QPen()

        pen.setWidth(2)
        pen.setColor(QColor(0, 0, 255))
        painter.setPen(pen)

        v_point = self.viewport_transformation(viewport)

        painter.drawPoint(v_point.to_QPointF())

from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QColor, QPainter, QPen
import numpy as np
import math as mt

# (300,350)
# (200,480)

class Point:
    def __init__(self, name, x, y, z):
        self.coordinates = [x, y, z]
        self.name = name
        self.type_object = "point"
        self.color = QColor(63, 145, 0)
        self.normalized_points = []

    def get_name(self):
        return self.name

    def get_x(self):
        return self.coordinates[0]

    def get_y(self):
        return self.coordinates[1]

    def get_z(self):
        return self.coordinates[2]

    def get_points(self):
        return [self]

    def get_center(self):
        return self

    def get_type_object(self):
        return self.type_object
        
    def get_color(self):
        return self.color
    
    def get_normalized_points(self):
        return self.normalized_points
        
    def set_x(self, x):
        self.coordinates[0] = x

    def set_y(self, y):
        self.coordinates[1] = y

    def set_z(self, z):
        self.coordinates[2] = z

    def set_color(self, color):
        self.color = color

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
        viewport_limits_points = [viewport.VCmaximum, viewport.VCminimum]
        normalized_viewport_limits = viewport.parent.display_window.generate_window_coords(viewport_limits_points)
        if not self.is_clipping(normalized_viewport_limits[0], normalized_viewport_limits[1]):
            painter = QPainter(viewport)
            pen = QPen()

            pen.setWidth(5)
            pen.setColor(self.color)
            painter.setPen(pen)

            # v_point = self.viewport_transformation(viewport)
            v_point = self.normalized_points[0].viewport_transformation(viewport)

            painter.drawPoint(v_point.to_QPointF())

    # Aplica as transformações no ponto
    def apply_transformation_point(self, matrix):
        current_point = np.array([self.get_x(), self.get_y(), self.get_z()])
        new_point = current_point.dot(matrix)
        # print(f'new point {new_point[0]}, {new_point[1]}')

        self.set_x(new_point[0])
        self.set_y(new_point[1])
        self.set_z(new_point[2])
    
    # Calcula as matrizes de transformações
    def apply_transformation(self, list_transformation):
        matrix = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        for i in list_transformation:
            matrix = matrix.dot(i.generate_matrix())
        
        self.apply_transformation_point(matrix)

    def set_normalized_coords(self, window):
        self.normalized_points = window.generate_window_coords(self.get_points())

    def is_clipping(self, maximum, minimum):
        point = self.get_normalized_points()[0]
        if point.get_x() >= minimum.get_x() and point.get_x() <= maximum.get_x() and point.get_y() >= minimum.get_y() and point.get_y() <= maximum.get_y():
            return False
        else:
            return True

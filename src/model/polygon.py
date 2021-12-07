from src.model.point import Point
from src.utils.object import GraphicObject
from PyQt5.QtGui import QColor, QPainter, QPen
import numpy as np

# (280,285),(300,320),(350,355)

class Polygon(GraphicObject):
    def __init__(self, name, points):
        super().__init__(name, points)
        self.center = self.set_center(points)
        self.points = points
        self.type_object = "polygon"
        self.color = QColor(0, 0, 255)

    # Calcula o centro do objeto
    def set_center(self, points):
        countX = 0
        countY = 0
        for point in points:
            countX += point.get_x()
            countY += point.get_y()
        centerX = countX / len(points)
        centerY = countY / len(points)
        center = Point("center", centerX, centerY, 1)
        return center

    def get_type_object(self):
        return self.type_object

    def get_name(self):
        return self.name

    def get_points(self):
        return self.point

    def get_center(self):
        return self.center

    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color

    # Aplica a transformada de viewport nos pontos do objeto e depois desenha
    def draw(self, viewport):
        painter = QPainter(viewport)
        pen = QPen()

        pen.setWidth(2)
        pen.setColor(self.color)
        painter.setPen(pen)

        v_points = []

        for point in self.get_normalized_points():
            v_points.append(point.viewport_transformation(viewport))

        for i in range(len(v_points) - 1):
            v_point_origin = v_points[i]
            v_point_destiny = v_points[i + 1]
            painter.drawLine(v_point_origin.to_QPointF(), v_point_destiny.to_QPointF())

        origin = v_points[0].to_QPointF()
        destiny = v_points[-1].to_QPointF()

        painter.drawLine(origin, destiny)

    def apply_transformation(self, list_transformation):
        matrix = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        for i in list_transformation:
            matrix = matrix.dot(i.generate_matrix())

        for point in self.points:
            # print(f'original {point.get_x()},{point.get_y()}')
            point.apply_transformation_point(matrix)
            # print(f'transformado {point.get_x()},{point.get_y()}')
        self.center = self.set_center(self.points)

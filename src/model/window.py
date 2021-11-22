from src.model.point import Point
from src.utils.object import GraphicObject
from PyQt5.QtGui import QColor, QPainter, QPen


class Window():
    def __init__(self):
        self.origin = Point("origin", 0, 0, 1)
        self.v_up_vector = 1

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
        print(f'center={center}')
        return center

    def get_name(self):
        return self.name

    def get_points(self):
        return self.point

    def get_center(self):
        return self.center

    
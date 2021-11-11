from src.model.point import Point
from src.utils.object import GraphicObject
from PyQt5.QtGui import QColor, QPainter, QPen


class Line(GraphicObject):
    def __init__(self, name, points):
        super().__init__(name, points)
        self.origin = points[0]
        self.destiny = points[1]
        self.center = self.Center(points)

    def Center(self, points):
        centerX = (points[0].get_x() + points[1].get_x()) / 2
        centerY = (points[0].get_y() + points[1].get_y()) / 2
        center = Point("point",centerX, centerY, 1)
        return center

    def getName(self):
        return self.name

    def getOrigin(self):
        return self.origin

    def getDestiny(self):
        return self.destiny

    def getCenter(self):
        return self.center

    def draw(self, viewport):
        painter = QPainter(viewport)
        pen = QPen()

        pen.setWidth(2)
        pen.setColor(QColor(0, 0, 255))
        painter.setPen(pen)

        v_point_origin = self.origin.viewport_transformation(viewport)
        v_point_destiny = self.destiny.viewport_transformation(viewport)

        painter.drawLine(v_point_origin.to_QPointF(), v_point_destiny.to_QPointF())
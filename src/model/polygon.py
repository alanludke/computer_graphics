from src.model.point import Point
from src.utils.object import GraphicObject


class Polygon(GraphicObject):
    def __init__(self, name, points):
        super().__init__(name, points)
        self.center = self.Center(points)
        self.points = points

    def Center(self, points):
        countX = 0
        countY = 0
        for point in points:
            countX += point.get_x()
            countY += point.get_y()
        centerX = countX / len(points)
        centerY = countY / len(points)
        center = Point(centerX, centerY, 1)
        return center

    def getName(self):
        return self.name

    def getPoints(self):
        return self.point

    def getCenter(self):
        return self.center


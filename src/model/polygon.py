from model.point import Point
from utils.object import GraphicObject

class Polygon(GraphicObject):
    def __init__(self, name, points):
        super().__init__(name, points)
        self.center = self.Center(points)
    
    def Center(points):
        countX = 0
        countY = 0
        for point in points:
            countX += point.get_x()
            countY += point.get_y()
        centerX = countX / points.len()
        centerY = countY / points.len()
        center = Point(centerX, centerY, 1)
        return center

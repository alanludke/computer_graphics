from src.model.point import Point
from src.utils.object import GraphicObject
# from model.graphic_object_enum import GraphicObjectEnum

class Line(GraphicObject):
    
    def __init__(self, name, points):
        super().__init__(name, points)
        self.origin = points[0]
        self.destiny = points[1]
        self.center = self.Center(points)

    def Center(self, points):
        centerX = (points[0].get_x() + points[1].get_x()) / 2
        centerY = (points[0].get_y() + points[1].get_y()) / 2
        center = Point(centerX, centerY, 1)
        return center

    def getName(self):
        return self.name
    
    def getOrigin(self):
        return self.origin
    
    def getDestiny(self):
        return self.destiny
    
    def getCenter(self):
        return self.center

from src.model.point import Point
from src.utils.object import GraphicObject
from PyQt5.QtGui import QColor, QPainter, QPen

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

    def draw(self, viewport):
        painter = QPainter(viewport)
        pen = QPen()

        pen.setWidth(2)
        pen.setColor(QColor(0, 0, 255))
        painter.setPen(pen)
        
        # v_point_origin = self.origin.viewport_transformation(viewport)
        # v_point_destiny = self.destiny.viewport_transformation(viewport)

        # painter.drawLine(v_point_origin.to_QPointF(), v_point_destiny.to_QPointF())
        
        v_points = []

        for point in self.points:
            v_points.append(point.viewport_transformation(viewport))
        
        for i in range(len(v_points)-1):
            v_point_origin = v_points[i].viewport_transformation(viewport)
            v_point_destiny = v_points[i+1].viewport_transformation(viewport)
            
            painter.drawLine(v_point_origin.to_QPointF(), v_point_destiny.to_QPointF())

        origin=v_points[0].viewport_transformation(viewport).to_QPointF()
        destiny=v_points[-1].viewport_transformation(viewport).to_QPointF()
        painter.drawLine(origin, destiny)


#(50,50),(50,425),(425,425)
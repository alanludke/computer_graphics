from src.model.point import Point
from src.utils.object import GraphicObject
from PyQt5.QtGui import QColor, QPainter, QPen
import numpy as np

#(100,100),(100,200)

class Line(GraphicObject):
    def __init__(self, name, points):
        super().__init__(name, points)
        self.origin = points[0]
        self.destiny = points[1]
        self.center = self.set_center(points)
        self.type_object = "line"
        self.color = QColor(255, 113, 0)

    # Calcula o centro do objeto
    def set_center(self, points):
        centerX = (points[0].get_x() + points[1].get_x()) / 2
        centerY = (points[0].get_y() + points[1].get_y()) / 2
        center = Point("point", centerX, centerY, 1)

        return center

    def get_name(self):
        return self.name

    def get_origin(self):
        return self.origin

    def get_destiny(self):
        return self.destiny

    def get_center(self):
        return self.center
    
    def get_points(self):
        return [self.origin, self.destiny]

    def get_type_object(self):
        return self.type_object
    
    def get_color(self):
        return self.color
        
    # Aplica a transformada de viewport nos pontos do objeto e depois desenha
    def draw(self, viewport):
        painter = QPainter(viewport)
        pen = QPen()

        pen.setWidth(2)
        pen.setColor(self.color)
        painter.setPen(pen)

        v_point_origin = self.origin.viewport_transformation(viewport)
        v_point_destiny = self.destiny.viewport_transformation(viewport)
        # print(len(self.normalized_points))
        # v_point_origin = self.get_normalized_points()[0].viewport_transformation(viewport)
        # v_point_destiny = self.get_normalized_points()[1].viewport_transformation(viewport)
        
        painter.drawLine(v_point_origin.to_QPointF(), v_point_destiny.to_QPointF())
        # painter.drawLine(viewport.generate_viewport_coords(v_point_origin).to_QPointF(), viewport.generate_viewport_coords(v_point_destiny).to_QPointF())

        pen.setColor(QColor(0, 0, 255))
        painter.setPen(pen)
        v_point_center = self.get_center().viewport_transformation(viewport)
        painter.drawPoint(v_point_center.to_QPointF())

    def apply_transformation(self, list_transformation):
        self.origin.apply_transformation(list_transformation)
        self.destiny.apply_transformation(list_transformation)
        self.center = self.set_center([self.origin, self.destiny])
    
    def set_normalized_coords(self, window):
        self.normalized_points = window.generate_window_coords(self.get_points())

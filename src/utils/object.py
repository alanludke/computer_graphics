from abc import abstractmethod
from typing import List

from PyQt5.QtGui import QPainter
from src.model.point import Point
# from model.graphic_object_enum import GraphicObjectEnum
#(1,2),(1,2)

class GraphicObject:

    def __init__(self, name, points):
        self.name = name
        self.point = points

    @abstractmethod
    def draw(self, painter: QPainter, viewport_min: Point, viewport_max: Point, viewport_origin: Point):
        ...

    def viewport_transform(point: Point, viewport_min: Point, viewport_max: Point, viewport_origin: Point) -> Point:
 
        window_min = Point(-1, -1)
        window_max = Point(1, 1)

        # x_div = (x_w - x_w_min) / (x_w_max - x_w_min)
        x_div = (point.x() - window_min.x()) / (window_max.x() - window_min.x())

        # x_v = x_div * (x_v_max - x_v_min)
        x_vp = x_div * (viewport_max.x() - viewport_min.x())

        # y_div = (y_w - y_w_min) / (y_w_max - y_w_min)
        y_div = (point.y() - window_min.y()) / (window_max.y() - window_min.y())

        # y_v = (1 - y_div) * (y_v_max - y_v_min)
        y_vp = (1 - y_div) * (viewport_max.y() - viewport_min.y())

        return Point(x_vp + viewport_origin.x(), y_vp + viewport_origin.y())

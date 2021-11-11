from typing import List
from PyQt5.QtGui import QColor, QPainter, QPen
from PyQt5.QtWidgets import QLabel
from src.model.line import Line
from src.model.polygon import Polygon
from src.model.point import Point
from src.utils.object import GraphicObject


class Viewport(QLabel):
    def __init__(self, parent):
        super(Viewport, self).__init__(parent)
        self.parent = parent
        self.objects = []
        self.origin = Point(0, 0, 1)

        # set borders
        self.stylesheet = """
            QLabel {
                background-color: white;
                border: 2px solid black
            }
        """
        self.width = 500
        self.height = 500

        self.setStyleSheet(self.stylesheet)
        self.setFixedWidth(self.width)
        self.setFixedHeight(self.height)

        # Viewport limits
        self.Vb_r = Point(self.width, self.height, 1)
        self.Vb_l = Point(self.height, 0, 1)
        self.Vt_l = self.origin
        self.Vt_r = Point(0, self.width, 1)

        # Window limits
        self.Wb_r = Point(475, 475, 1)
        self.Wb_l = Point(25, 475, 1)
        self.Wt_l = Point(25, 25, 1)
        self.Wt_r = Point(475, 25, 1)

    def draw_borders(self):
        painter = QPainter(self)
        pen = QPen()

        pen.setWidth(2)
        pen.setColor(QColor(255, 0, 1))
        painter.setPen(pen)

        painter.drawLine(self.Wt_r.to_QPointF(), self.Wt_l.to_QPointF())
        painter.drawLine(self.Wt_r.to_QPointF(), self.Wb_r.to_QPointF())
        painter.drawLine(self.Wb_l.to_QPointF(), self.Wb_r.to_QPointF())
        painter.drawLine(self.Wb_l.to_QPointF(), self.Wt_l.to_QPointF())

    def draw_cross(self):
        painter = QPainter(self)
        pen = QPen()

        pen.setWidth(2)
        pen.setColor(QColor(0, 255, 0))
        painter.setPen(pen)

        m_t = Point(250, 25, 1).to_QPointF()
        m_b = Point(250, 475, 1).to_QPointF()
        m_l = Point(25, 250, 1).to_QPointF()
        m_r = Point(475, 250, 1).to_QPointF()

        painter.drawLine(m_t, m_b)
        painter.drawLine(m_l, m_r)

    def paintEvent(self, event):
        self.draw_borders()
        self.draw_cross()

        for obj in self.objects:
            if isinstance(obj, Point):
                print("point chris")
                obj.draw(self)
            elif isinstance(obj, Line):
                print("line drew")
                obj.draw(self)
            elif isinstance(obj, Polygon):
                print("poligon tonia")
                obj.draw(self)

    def draw_objects(self, objects: List[GraphicObject]):
        self.objects = objects
        self.update()

    def viewport_transform(self, point: Point) -> Point:

        window_min = self.Wb_l
        window_max = self.Wt_r
        viewport_max = self.Vt_r
        viewport_min = self.Vb_l

        # x_div = (x_w - x_w_min) / (x_w_max - x_w_min)
        x_div = (point.get_x() - window_min.get_x()) / (window_max.get_x() - window_min.get_x())

        # x_v = x_div * (x_v_max - x_v_min)
        x_vp = x_div * (viewport_max.get_x() - viewport_min.get_x())

        # y_div = (y_w - y_w_min) / (y_w_max - y_w_min)
        y_div = (point.get_y() - window_min.get_y()) / (window_max.get_y() - window_min.get_y())

        # y_v = (1 - y_div) * (y_v_max - y_v_min)
        y_vp = (1 - y_div) * (viewport_max.get_y() - viewport_min.get_y())

        return Point(x_vp + self.origin.get_x(), y_vp + self.origin.get_y(), 1)
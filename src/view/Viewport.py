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
        self.origin = Point(0,0,1)
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

    def draw_borders(self):
        painter = QPainter(self)
        pen = QPen()

        pen.setWidth(2)
        pen.setColor(QColor(255, 0, 1))
        painter.setPen(pen)

        b_r = Point(475, 475, 1).to_QPointF()
        b_l = Point(25, 475, 1).to_QPointF()
        t_l = Point(25, 25, 1).to_QPointF()
        t_r = Point(475, 25, 1).to_QPointF()

        painter.drawLine(t_r, t_l)
        painter.drawLine(t_r, b_r)
        painter.drawLine(b_l, b_r)
        painter.drawLine(b_l, t_l)

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
        painter = QPainter(self)
        pen = QPen()
        # self.draw_borders()
        # self.draw_cross()

        for obj in self.objects:
            print(f'type(obj)={type(obj)}')
            if isinstance(obj, Point):
                print('point chris')
                obj.draw(self)
            elif isinstance(obj, Line):
                print('line drew')
                obj.draw(self)
            elif isinstance(obj, Polygon):
                print('poligon tonia')
                obj.draw(self)
            # self.draw(painter, self.coordinates[0], self.coordinates[1], self.origin)

    def draw_objects(self, objects: List[GraphicObject]):
        self.objects = objects
        self.update()
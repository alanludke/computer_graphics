import sys
from typing import List
from PyQt5 import QtGui
from PyQt5.QtGui import QColor, QPainter, QPen
from PyQt5.QtWidgets import QLabel, QWidget
from src.model.point import Point


class Viewport(QLabel):
    def __init__(self):
        super().__init__()

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

        # self.t_l = [25, 25]
        # self.t_r = [475, 25]
        # self.b_l = [25, 475]
        # self.b_r = [475, 475]

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
        self.draw_borders()
        self.draw_cross()

    # def viewportTransform(self):
    #     pass
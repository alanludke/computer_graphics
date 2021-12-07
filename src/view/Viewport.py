from typing import List
from PyQt5.QtGui import QColor, QPainter, QPen, QWheelEvent
from PyQt5.QtWidgets import QAction, QLabel
from src.model.line import Line
from src.model.polygon import Polygon
from src.model.point import Point
from src.utils.object import GraphicObject


class Viewport(QLabel):
    def __init__(self, parent):
        super(Viewport, self).__init__(parent)
        self.parent = parent
        self.objects = []
        self.origin = Point("origin", 0, 0, 1)

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
        self.Vb_r = Point("Vb_r", self.width, self.height, 1)
        self.Vb_l = Point("Vb_l", self.height, 0, 1)
        self.Vt_l = Point("Vt_l", self.origin.get_x(), self.origin.get_y(), 1)
        self.Vt_r = Point("Vt_r", 0, self.width, 1)

        # Window limits
        self.Wb_r = Point("Wb_r", 475, 475, 1)
        self.Wb_l = Point("Wb_l", 25, 475, 1)
        self.Wt_l = Point("Wt_l", 25, 25, 1)
        self.Wt_r = Point("Wt_r", 475, 25, 1)

    def get_center(self):
        return Point("Window_Center", self.width / 2, self.height / 2, 1)

    # Desenha as bordas da Window
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

    # Desenha as linhas verticais no centro da Window
    def draw_cross(self):
        painter = QPainter(self)
        pen = QPen()

        pen.setWidth(2)
        pen.setColor(QColor(0, 0, 0))
        painter.setPen(pen)

        m_t = Point("m_t", 250, 25, 1).to_QPointF()
        m_b = Point("m_b", 250, 475, 1).to_QPointF()
        m_l = Point("m_l", 25, 250, 1).to_QPointF()
        m_r = Point("m_r", 475, 250, 1).to_QPointF()

        painter.drawLine(m_t, m_b)
        painter.drawLine(m_l, m_r)

    # Desenha as linhas verticais no centro da Window
    def draw_center(self):  # da pra apagar?
        painter = QPainter(self)
        pen = QPen()

        pen.setWidth(2)
        pen.setColor(QColor(115, 93, 13))
        painter.setPen(pen)

        painter.drawLine(self.get_center().to_QPointF(), self.get_center().to_QPointF())

    # Desenha um novo objeto recém criado
    def paintEvent(self, event):
        self.draw_borders()
        self.draw_cross()
        self.draw_center()

        for obj in self.objects:
            if isinstance(obj, Point):
                obj.draw(self)
            elif isinstance(obj, Line):
                obj.draw(self)
            elif isinstance(obj, Polygon):
                obj.draw(self)

    def draw_objects(self, objects: List[GraphicObject]):
        self.objects = objects
        self.update()

    # Realiza a transformada de Viewport sobre um ponto
    def viewport_transform(self, point: Point) -> Point:
        window_min = self.Wb_l
        window_max = self.Wt_r
        viewport_max = self.Vb_r
        viewport_min = self.Vt_l

        # x_div = (x_w - x_w_min) / (x_w_max - x_w_min)
        x_div = (point.get_x() - window_min.get_x()) / (
            window_max.get_x() - window_min.get_x()
        )

        # x_v = x_div * (x_v_max - x_v_min)
        x_vp = x_div * (viewport_max.get_x() - viewport_min.get_x())

        # y_div = (y_w - y_w_min) / (y_w_max - y_w_min)
        y_div = (point.get_y() - window_min.get_y()) / (
            window_max.get_y() - window_min.get_y()
        )

        # y_v = (1 - y_div) * (y_v_max - y_v_min)
        y_vp = (1 - y_div) * (viewport_max.get_y() - viewport_min.get_y())

        return Point(
            "point transformed",
            x_vp + self.origin.get_x(),
            y_vp + self.origin.get_y(),
            1,
        )

    def generate_viewport_coords(self, points):
        x = (500 - 0) / (1 + 1) * (points.get_x() - (-1))
        y = (500 - 0) / (1 + 1) * (points.get_y() - (-1))
        v_point = Point(points.get_name(), x, y, 1)
        return v_point
        # viewport_coords = []
        # for point in points:
        #     # formula para desnormalização x = xwmin + ((xwmax - xwmin) / (xvmax-xvmin))*xv - xvmin
        #     x = (500 - 0) / (1 + 1) * (point.get_x() - (-1))
        #     y = (500 - 0) / (1 + 1) * (point.get_y() - (-1))
        #     v_point = Point(point.get_name(), x, y, 1)
        #     viewport_coords.append(v_point)

        # return viewport_coords

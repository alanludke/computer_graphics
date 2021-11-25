from src.model.point import Point
from src.utils.object import GraphicObject
from PyQt5.QtGui import QColor, QPainter, QPen


class Polygon(GraphicObject):
    def __init__(self, name, points):
        super().__init__(name, points)
        self.center = self.set_center(points)
        self.points = points
        self.type = "polygon"
        self.color = QColor(0, 0, 255)

    # (280,285),(300,320),(350,355)

    # Calcula o centro do objeto
    def set_center(self, points):
        countX = 0
        countY = 0
        for point in points:
            countX += point.get_x()
            countY += point.get_y()
        centerX = countX / len(points)
        centerY = countY / len(points)
        center = Point("center", centerX, centerY, 1)
        # print(f'center={center}')
        return center

    def get_type(self):
        return self.type

    def get_name(self):
        return self.name

    def get_points(self):
        return self.point

    def get_center(self):
        return self.center

    def get_color(self):
        return self.color

    # Aplica a transformada de viewport nos pontos do objeto e depois desenha
    def draw(self, viewport):
        painter = QPainter(viewport)
        pen = QPen()

        pen.setWidth(2)
        pen.setColor(self.color)
        painter.setPen(pen)

        v_points = []

        for point in self.points:
            v_points.append(point.viewport_transformation(viewport))

        for i in range(len(v_points) - 1):
            v_point_origin = v_points[i].viewport_transformation(viewport)
            v_point_destiny = v_points[i + 1].viewport_transformation(viewport)

            painter.drawLine(v_point_origin.to_QPointF(), v_point_destiny.to_QPointF())

        origin = v_points[0].viewport_transformation(viewport).to_QPointF()
        destiny = v_points[-1].viewport_transformation(viewport).to_QPointF()

        v_point_center = self.get_center().viewport_transformation(viewport)
        painter.drawLine(origin, destiny)

        # painter.drawPoint(v_point_center.to_QPointF())

    def apply_transformation(self, list_transformation):
        for point in self.points:
            point.apply_transformation(list_transformation)
        self.center = self.set_center(self.points)

    def set_normalized_coords(self, window):
        self.normalized_points = window.generate_window_coords(self.get_points())
from src.model.point import Point
from src.utils.object import GraphicObject
from PyQt5.QtGui import QColor, QPainter, QPen


class Window():
    def __init__(self, w_center):
        self.origin = Point("origin", 0, 0, 1)
        self.w_center_position = Point("w_center_position", w_center[0], w_center[1], 1)
        self.v_up_vector = 1
        self.minimum = Point("w_minimum", -1, -1, 1)
        self.maximum = Point("w_maximum", 1, 1, 1)

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

        return center

    def get_name(self):
        return self.name

    def get_points(self):
        return self.point

    def get_center(self):
        return self.center

    def generate_window_coords(self, points):
        normalized_points = []
        for point in points:
            # formula para normalização x = xwmin + ((xwmax - xwmin) / (xvmax-xvmin))*xv - xvmin
            x = self.minimum.get_x() + ((self.maximum.get_x() - self.minimum.get_x()) / (500 - 0)) * (point.get_x() - 0)
            y = self.minimum.get_y() + ((self.maximum.get_y() - self.minimum.get_y()) / (500 - 0)) * (point.get_y() - 0)
            n_point = Point(point.get_name(), x, y, 1)
            normalized_points.append(n_point)
            print(f'tamnho de normalized points: {len(normalized_points)}')

        return normalized_points  
    
        # 0. Crie ou mova a window onde desejar;

        # 1. Translade Wc para a origem;
        # Translade o mundo de [-Wcx, -Wcy].

        # 2. Determine vup e o ângulo de vup com Y

        # 3. Rotacione o mundo de forma a alinhar vup com o
        # eixo Y;
        # Rotacione o mundo por -θ(Y, vup).

        # 4. Normalize o conteúdo da window, realizando um
        # escalonamento do mundo;

        # 5. Armazene as coordenadas SCN de cada objeto.
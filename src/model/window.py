from src.model.point import Point
from src.utils.object import GraphicObject
from PyQt5.QtGui import QColor, QPainter, QPen


class Window():
    def __init__(self):
        self.origin = Point("origin", 0, 0, 1)
        self.v_up_vector = 1

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
        print(f'center={center}')
        return center

    def get_name(self):
        return self.name

    def get_points(self):
        return self.point

    def get_center(self):
        return self.center

    def generate_window_coords(self):
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


        pass




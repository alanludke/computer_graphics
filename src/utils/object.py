from abc import abstractmethod
from typing import List

from PyQt5.QtGui import QPainter
from src.model.point import Point


class GraphicObject:
    def __init__(self, name, points):
        self.name = name
        self.point = points
        self.normalized_points = []

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
    
    def get_points(self):
        return self.point

    def get_normalized_points(self):
        return self.normalized_points

    def set_normalized_points(self, points):
        pass
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

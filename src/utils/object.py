from abc import abstractmethod
from typing import List

from PyQt5.QtGui import QPainter
from src.model.point import Point


class GraphicObject:
    def __init__(self, name, points):
        self.name = name
        self.point = points

    def get_name(self):
        return self.name

    def get_points(self):
        return self.point
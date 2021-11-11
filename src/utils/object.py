from abc import abstractmethod
from typing import List

from PyQt5.QtGui import QPainter
from src.model.point import Point

# from model.graphic_object_enum import GraphicObjectEnum
# (1,2),(1,2)


class GraphicObject:
    def __init__(self, name, points):
        self.name = name
        self.point = points

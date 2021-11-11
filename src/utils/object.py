from abc import abstractmethod
from typing import List

from PyQt5.QtGui import QPainter
from src.model.point import Point

class GraphicObject:
    def __init__(self, name, points):
        self.name = name
        self.point = points

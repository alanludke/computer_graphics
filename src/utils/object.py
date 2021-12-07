from abc import abstractmethod
from typing import List

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

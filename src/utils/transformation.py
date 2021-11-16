from abc import abstractmethod
from typing import List

from PyQt5.QtGui import QPainter
import numpy as np
import math as mt
from src.model.point import Point


class Transformation:
    def __init__(self, action, x, y):
        if action == "Escalonar" or action == "Transladar":
            self.action = action
            self.factor_x = x
            self.factor_y = y
            self.factor_z = 1
        else:
            self.action = action
            self.reference_point = x
            self.angle = y
        self.matrix = self.generate_matrix()

    def getAction(self):
        return self.action

    def getMatrix(self):
        return self.matrix

    def generate_matrix(self):
        if self.action == "Escalonar":
            return np.array([[1, 0, 0], [0, 1, 0], [self.factor_x, self.factor_y, 1]])
        elif self.action == "Transladar":
            return np.array([[self.factor_x, 0, 0], [0, self.factor_y, 0], [0, 0, 1]])
        else:
            cos_angle = mt.cos(self.angle)
            sin_angle = mt.sin(self.angle)
            return np.array(
                [[cos_angle, -sin_angle, 0], [sin_angle, cos_angle, 0], [0, 0, 1]]
            )

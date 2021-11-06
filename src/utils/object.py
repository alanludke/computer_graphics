from typing import List
from model.point import Point
from model.graphic_object_enum import GraphicObjectEnum

class GraphicObject:
    def __init__(self, name:str, type:GraphicObjectEnum, coordinates: List[Point]):
        self.name = name
        self.type = type
        self.coordinates = coordinates
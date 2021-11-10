from enum import Enum

class GraphicObjectEnum(Enum):
    POINT = "Point"
    LINE = "Line"
    POLYGON = "Polygon"

    def value(v: str):
        for goe in GraphicObjectEnum:
            if v == goe.value:
                return goe
        return None
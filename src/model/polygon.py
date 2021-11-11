from src.model.point import Point
from src.utils.object import GraphicObject

class Polygon(GraphicObject):
    def __init__(self, name, points):
        super().__init__(name, points)
        self.center = self.Center(points)
        self.points = points
    
    def Center(self,points):
        countX = 0
        countY = 0
        for point in points:
            countX += point.get_x()
            countY += point.get_y()
        centerX = countX / len(points)
        centerY = countY / len(points)
        center = Point(centerX, centerY, 1)
        return center
    
    def getName(self):
        return self.name

    def getPoints(self):
        return self.point
    
    def getCenter(self):
        return self.center


# def main():
#     """Função principal da aplicação.
#     """
#     p1 = Point(100,200,3)
#     p2 = Point(400,300,5)
#     p3 = Point(300,400,1)
#     p=Polygon('poligon',[p1,p2,p3])
#     print(p.getCenter())

# if __name__ == "__main__":
#     main()
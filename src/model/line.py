from src.model.point import Point
from src.utils.object import GraphicObject
from PyQt5.QtGui import QColor, QPainter, QPen
import numpy as np

#(100,100),(100,300)
#(250,250),(400,250)
#(250,250),(300,350)
#(15,400),(300,300)

class Line(GraphicObject):
    def __init__(self, name, points):
        super().__init__(name, points)
        self.origin = points[0]
        self.destiny = points[1]
        self.center = self.set_center(points)
        self.type_object = "line"
        self.color = QColor(255, 113, 0)

    # Calcula o centro do objeto
    def set_center(self, points):
        centerX = (points[0].get_x() + points[1].get_x()) / 2
        centerY = (points[0].get_y() + points[1].get_y()) / 2
        center = Point("point", centerX, centerY, 1)

        return center

    def get_name(self):
        return self.name

    def get_origin(self):
        return self.origin

    def get_destiny(self):
        return self.destiny

    def get_center(self):
        return self.center
    
    def get_points(self):
        return [self.origin, self.destiny]

    def get_type_object(self):
        return self.type_object
    
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color
        
    # Aplica a transformada de viewport nos pontos do objeto e depois desenha
    def draw(self, viewport):
        painter = QPainter(viewport)
        pen = QPen()

        pen.setWidth(2)
        pen.setColor(self.color)
        painter.setPen(pen)
        
        viewport_limits_points = [viewport.VCmaximum, viewport.VCminimum]
        normalized_viewport_limits = viewport.parent.display_window.generate_window_coords(viewport_limits_points)
        clipping_points = self.clipping_Liang_Barsky(normalized_viewport_limits[0], normalized_viewport_limits[1])
        if len(clipping_points) > 0:
            v_point_origin = clipping_points[0].viewport_transformation(viewport)
            v_point_destiny = clipping_points[1].viewport_transformation(viewport)
            painter.drawLine(v_point_origin.to_QPointF(), v_point_destiny.to_QPointF())

    def apply_transformation(self, list_transformation):
        matrix = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        for i in list_transformation:
            matrix = matrix.dot(i.generate_matrix())
        self.origin.apply_transformation_point(matrix)
        self.destiny.apply_transformation_point(matrix)
        self.center = self.set_center([self.origin, self.destiny])

    def clipping_Liang_Barsky(self, w_maximum, w_minimum):
        delta_x = self.get_normalized_points()[1].get_x() - self.get_normalized_points()[0].get_x()
        delta_y = self.get_normalized_points()[1].get_y() - self.get_normalized_points()[0].get_y()
        
        p1 = - (delta_x)
        p2 = delta_x
        p3 = - (delta_y)
        p4 = delta_y
        pk = [p1, p2, p3, p4]
        zeta1 = 0
        zeta2 = 0
        clipping_points = []

        origin = self.get_normalized_points()[0]
        destiny = self.get_normalized_points()[1]

        q1 = origin.get_x() - w_minimum.get_x()
        q2 = w_maximum.get_x() - origin.get_x()
        q3 = origin.get_y() - w_minimum.get_y()
        q4 = w_maximum.get_y() - origin.get_y()
        qk = [q1, q2, q3, q4]
        positive_pk = []
        negative_pk = []
        for p in range(len(pk)):
            if pk[p] < 0:
                r = qk[p] / pk[p]
                negative_pk.append(r)  
            elif pk[p] > 0:
                r = qk[p] / pk[p]
                positive_pk.append(r) 
            elif pk[p] == 0: # reta fora dos limites, arrumar !!!
                if qk[p] < 0:
                    print("reta fora dos limites")
                    return clipping_points
                else:
                    positive_pk.append(qk[p])

        temp1 = max(negative_pk)
        zeta1 = max(0, temp1)
        print(f'{zeta1} -> zeta 1')
        temp2 = min(positive_pk)
        zeta2 = min(1, temp2)
        print(f'{zeta2} -> zeta 2')

        if zeta1 > zeta2:
            return clipping_points
        else:
            if not zeta1 == 0 and zeta2 == 1:
                x = origin.get_x() + zeta1 * delta_x
                y = origin.get_y() + zeta1 * delta_y
                new_point = Point("clipping_point", x, y, 1)
                print(f'zeta 1 {new_point.get_x()}, {new_point.get_y()}')
                clipping_points = [new_point, destiny]
            elif zeta1 == 0:
                clipping_points.append(origin)
            
            if not zeta2 == 1 and zeta1 == 0:
                x = origin.get_x() + zeta2 * delta_x
                y = origin.get_y() + zeta2 * delta_y
                new_point = Point("clipping_point", x, y, 1)
                print(f'zeta 2 {new_point.get_x()}, {new_point.get_y()}')
                clipping_points = [origin, new_point]
            elif zeta2 == 1:
                clipping_points.append(destiny)
            
            if not zeta1 == 0 and not zeta2 == 1:
                x_origin = origin.get_x() + zeta1 * delta_x
                y_origin = origin.get_y() + zeta1 * delta_y
                x_destiny = origin.get_x() + zeta2 * delta_x
                y_destiny = origin.get_y() + zeta2 * delta_y
                new_origin = Point("clipping_point_origin", x_origin, y_origin, 1)
                new_destiny = Point("clipping_point_destiny", x_destiny, y_destiny, 1) 
                clipping_points = [new_origin, new_destiny] 

        return clipping_points

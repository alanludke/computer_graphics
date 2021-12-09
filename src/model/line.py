from src.model.point import Point
from src.utils.object import GraphicObject
from PyQt5.QtGui import QColor, QPainter, QPen
import numpy as np

#(100,100),(100,200)
#(250,250),(260,260)
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

        v_point_origin = None 
        v_point_destiny = None
        
        viewport_limits_points = [viewport.VCmaximum, viewport.VCminimum]
        normalized_viewport_limits = viewport.parent.display_window.generate_window_coords(viewport_limits_points)
        is_clipping_line = self.is_clipping(normalized_viewport_limits[0], normalized_viewport_limits[1])
        clipping_points = is_clipping_line[1]

        if not is_clipping_line[0]:
            v_point_origin = self.get_normalized_points()[0].viewport_transformation(viewport)
            v_point_destiny = self.get_normalized_points()[1].viewport_transformation(viewport)
        
        else:
            new_point = self.clipping_Liang_Barsky(normalized_viewport_limits[0], normalized_viewport_limits[1], clipping_points)
            v_point_origin = new_point[0].viewport_transformation(viewport)
            v_point_destiny = self.get_normalized_points()[1].viewport_transformation(viewport)
            # v_point_origin = new_point[1].viewport_transformation(viewport)
            print(f'origin ({v_point_origin.get_x()},{v_point_origin.get_x()})')
            print(f'destiny ({v_point_destiny.get_x()},{v_point_destiny.get_y()})')

        painter.drawLine(v_point_origin.to_QPointF(), v_point_destiny.to_QPointF())

    def apply_transformation(self, list_transformation):
        matrix = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        for i in list_transformation:
            matrix = matrix.dot(i.generate_matrix())
        self.origin.apply_transformation_point(matrix)
        self.destiny.apply_transformation_point(matrix)
        self.center = self.set_center([self.origin, self.destiny])

    def is_clipping(self, maximum, minimum):
        points = self.get_normalized_points()
        out_points = []
        bool_clipping = False
        for point in points:
            if point.get_x() >= minimum.get_x() and point.get_x() <= maximum.get_x() and point.get_y() >= minimum.get_y() and point.get_y() <= maximum.get_y():
                bool_clipping = bool_clipping or False
            else:
                bool_clipping = bool_clipping or True
                out_points.append(point)
        return [bool_clipping, out_points]

    def clipping_Liang_Barsky(self, w_maximum, w_minimum, points):
        delta_x = self.get_normalized_points()[1].get_x() - self.get_normalized_points()[0].get_x()
        delta_y = self.get_normalized_points()[1].get_y() - self.get_normalized_points()[0].get_y()
        
        p1 = - (delta_x)
        p2 = delta_x
        p3 = - (delta_y)
        p4 = delta_y
        pk = [p1, p2, p3, p4]
        rk = []
        zeta1 = 0
        zeta2 = 0
        clipping_points = []

        for point in points:
        # point = self.get_normalized_points()[0]
            q1 = point.get_x() - w_minimum.get_x()
            q2 = w_maximum.get_x() - point.get_x()
            q3 = point.get_y() - w_minimum.get_y()
            q4 = w_maximum.get_y() - point.get_y()
            qk = [q1, q2, q3, q4]
            # rk = [q1/p1, q2/p2, q3/p3, q4/p4]
            positive_pk = []
            negative_pk = []
            for p in range(len(pk)):
                if pk[p] < 0:
                    negative_pk.append(qk[p] / pk[p])  
                elif pk[p] > 0:
                   positive_pk.append(qk[p] / pk[p]) 
                elif pk[p] == 0: # reta fora dos limites
                    if qk[p] < 0:
                        return clipping_points
                    else:
                        positive_pk.append(qk[p])

            temp1 = max(negative_pk)
            zeta1 = max(0, temp1)
            print(f'{zeta1} -> zeta 1')
            temp2 = min(positive_pk)
            zeta2 = min(1, temp2)
            print(f'{zeta2} -> zeta 2')

            if not zeta1 == 0:
                x = point.get_x() + zeta1 * delta_x
                y = point.get_y() + zeta1 * delta_y
                new_point = Point("clipping_point", x, y, 1)
                print(f'zeta 1 {new_point.get_x()}, {new_point.get_y()}')
                clipping_points.append(new_point)
            elif not zeta2 == 1:
                x = point.get_x() + zeta2 * delta_x
                y = point.get_y() + zeta2 * delta_y
                new_point = Point("clipping_point", x, y, 1)
                print(f'zeta 2 {new_point.get_x()}, {new_point.get_y()}')
                clipping_points.append(new_point)
            elif zeta1 > zeta2:
                return clipping_points

        return clipping_points
    
    # def clipping_Liang_Barsky(self, w_maximum, w_minimum):
    #     new_points = []
    #     # delta_x = self.destiny.get_x() - self.origin.get_x()
    #     # delta_y = self.destiny.get_y() - self.origin.get_y()
    #     delta_x = self.get_normalized_points()[1].get_x() - self.get_normalized_points()[0].get_x()
    #     delta_y = self.get_normalized_points()[1].get_y() - self.get_normalized_points()[0].get_y()
        
    #     p1 = - (delta_x)
    #     p2 = delta_x
    #     p3 = - (delta_y)
    #     p4 = delta_y

    #     pk = [p1, p2, p3, p4]
    #     rk = []
    #     zeta1 = 0
    #     zeta2 = 0
        
    #     for point in self.get_normalized_points():
    #         q1 = point.get_x() - w_minimum.get_x()
    #         q2 = w_maximum.get_x() - point.get_x()
    #         q3 = point.get_y() - w_minimum.get_y()
    #         q4 = w_maximum.get_y() - point.get_y()
    #         rk = [q1/p1, q2/p2, q3/p3, q4/p4]
    #         positive_pk = []
    #         negative_pk = []
    #         for p in range(len(pk)):
    #             if pk[p] < 0:
    #                 negative_pk.append(rk[p])  
    #             elif pk[p] > 0:
    #                 positive_pk.append(rk[p])                  

    #         temp1 = max(negative_pk)
    #         zeta1 = max(0, temp1)
    #         temp2 = min(positive_pk)
    #         zeta2 = min(1, temp2)

    #         if not zeta1 == 0:
    #             x = point.get_x() + zeta1 * delta_x
    #             y = point.get_y() + zeta1 * delta_y
    #             new_point = Point("clipping_point", x, y, 1)
    #             print(f'zeta 1 {new_point.to_QPointF}')
    #             new_points.append(new_point)
            
    #         if not zeta2 == 1:
    #             x = point.get_x() + zeta2 * delta_x
    #             y = point.get_y() + zeta2 * delta_y
    #             new_point = Point("clipping_point", x, y, 1)
    #             print(f'zeta 1 {new_point.to_QPointF}')
    #             new_points.append(new_point)

    #     return new_points

    def clipping(self):
        pass

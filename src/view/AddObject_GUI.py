import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from src.model.point import Point
from src.model.polygon import Polygon
from src.model.line import Line


class AddObject_GUI(QDialog):
    def __init__(self, parent):
        super(AddObject_GUI, self).__init__(parent)
        self.initUI()
        self.parent = parent


    def initUI(self):
        uic.loadUi("src/view/new_object_gui.ui", self)
        # self.txt_coord = 'afs'
        # buttons
        self.txt_coord.setPlaceholderText("(x0,y0,z0),(xn,yn,zn)")
        self.btn_add.clicked.connect(self.btn_add_clicked)

    def btn_add_clicked(self):
        input_name = self.txt_object_name.toPlainText()
        input_coord = self.txt_coord.toPlainText()

        num_coord = input_coord.split("),(")
        object_coord = self.getObjectCoord(num_coord)

        object = self.createObject(input_name, object_coord, len(num_coord))
        self.parent.addObjectDisplayFile(object)

        self.parent.terminal_out.append("btn_add clicked!!!")
        print("btn_add clicked")
        self.parent.viewport.draw_objects(self.parent.getDisplayFile())


#(0,1),(100,244),(200,300)

    def getObjectCoord(self, num_coord):
        cleaned = list(map(lambda x: x.replace('(','').replace(')',''), num_coord))
        list_of_points = []
        for each in cleaned:
            nums=each.split(',')
            print(f'nums={nums}')
            point= Point(int(nums[0]), int(nums[1]), 1)
            list_of_points.append(point)
        
        return list_of_points

    def createObject(self, name, coord, count_coord):
        object = None
        if(count_coord == 1):
            print('PONTO')
            object = Point(100, 200, 1)
        elif(count_coord == 2):
            print('LINHA')
            object = Line(name, coord)
        elif(count_coord > 2):
            print('POLIGINO')
            object = Polygon(name, coord)
        return object

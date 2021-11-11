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

        # buttons
        self.txt_coord.setPlaceholderText("(x0,y0,z0),(xn,yn,zn)")
        self.btn_add.clicked.connect(self.btn_add_clicked)

    def btn_add_clicked(self):
        input_name = self.txt_object_name.toPlainText()
        input_coord = self.txt_coord.toPlainText()
        num_coord = input_coord.split("),(")
        #(1,2),(3,4) ---> ['(1,2','3,4)']
        cleaned = list(map(lambda x: x.replace('(','').replace(')',''), num_coord))
        print(f'cleaned={cleaned}')
        list_of_points = []
        for each in cleaned:
            nums=each.split(',')
            #(1,2)
            print(f'nums={nums}')
            point= Point(int(nums[0]), int(nums[1]), 1)
            list_of_points.append(point)

        count_coord = len(num_coord)
        object_coord = self.getObjectCoord(num_coord)

        object = self.createObject(input_name, object_coord, count_coord)
        self.parent.addObjectDisplayFile(object)

        self.parent.terminal_out.append("btn_add clicked!!!")
        print("btn_add clicked")

    def getObjectCoord(self, coord):
        object_coord = coord
        for i in object_coord:
            i.replace("(", "")
            i.replace(")", "")
        
        for i in object_coord:
            i.split(",")
        
        return object_coord

    def createObject(self, name, coord, count_coord):
        object = None
        if(count_coord == 2):
            print('LINHA')
            object = Line(name, coord)
        elif(count_coord > 2):
            print('POLIGINO')
            object = Polygon(name, coord)
        return object
#(0,1),(100,244)

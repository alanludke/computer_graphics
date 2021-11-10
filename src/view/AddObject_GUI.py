import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from model.polygon import Polygon
from model.line import Line


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
        num_coord = input_coord.spli(",")
        count_coord = num_coord.len()
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
            object = Line(name, coord)
        elif(count_coord > 2):
            object = Polygon(name, coord)
        
        return object
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from src.model.point import Point
from src.model.polygon import Polygon
from src.model.line import Line

# Classe responsável pelo Frame onde são criados os objetos
class AddObject_GUI(QDialog):
    # Método construtor
    def __init__(self, parent):
        super(AddObject_GUI, self).__init__(parent)
        self.initUI()
        self.parent = parent

    # Inicializa componentes da interface, layouts e botões
    def initUI(self):
        uic.loadUi("src/view/add_object_gui.ui", self)
        # buttons
        self.txt_coord.setPlaceholderText("(x0,y0),(xn,yn)")
        self.btn_add.clicked.connect(self.btn_add_clicked)

    # Método de gatilho para quando objeto "Add object" é apertado
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

    # Método que retorna as coordenadas limpas de uma lista de
    def getObjectCoord(self, num_coord):
        cleaned = list(map(lambda x: x.replace("(", "").replace(")", ""), num_coord))
        list_of_points = []
        for each in cleaned:
            nums = each.split(",")
            point = Point("point", int(nums[0]), int(nums[1]), 1)
            list_of_points.append(point)

        return list_of_points

    # Método responsável por criar um objeto dependendo de seu tipo
    def createObject(self, name, coord, count_coord):
        object = None
        if count_coord == 1:
            object = Point(name, 100, 200, 1)
        elif count_coord == 2:
            object = Line(name, coord)
        elif count_coord > 2:
            object = Polygon(name, coord)
        return object

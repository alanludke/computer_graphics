import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *

from src.view.AddObject_GUI import AddObject_GUI
from src.view.TransformObject_GUI import TransformObject_GUI
from src.view.Viewport import Viewport
from src.view.ListObject import ListObject

# Classe responsável pela interface principal de interação
class Main_GUI(QMainWindow):
    # Método construtor da interface principal
    def __init__(self):
        super(Main_GUI, self).__init__()
        self.init_ui()
        self.display_file = []

    # Inicializa componentes da interface, layouts e botões
    def init_ui(self):
        uic.loadUi("src/view/main_gui.ui", self)
        self.show()
        self.viewport = Viewport(self)
        self.layout_viewport.addWidget(self.viewport)

        # Lista de objetos
        self.list_objects = ListObject(self)
        self.layout_list_objects.addWidget(self.list_objects)

        # buttons
        self.btn_add_object.clicked.connect(self.btn_add_object_clicked)
        self.btn_transform_object.clicked.connect(self.btn_transform_object_clicked)
        self.btd_frame_up.clicked.connect(self.btd_frame_up_clicked)
        self.btd_frame_down.clicked.connect(self.btd_frame_down_clicked)
        self.btd_frame_right.clicked.connect(self.btd_frame_right_clicked)
        self.btd_frame_left.clicked.connect(self.btd_frame_left_clicked)
        self.btd_frame_in.clicked.connect(self.btd_frame_in_clicked)
        self.btd_frame_out.clicked.connect(self.btd_frame_out_clicked)

    # Método que calcula o passo de movimentação da window
    def calculate_step(self, input):
        step = (self.viewport.width * input) / 100
        return step

    # Método de gatilho para quando objeto "Up" é apertado    
    def btd_frame_up_clicked(self):
        input = int(self.txt_step.text())
        step = self.calculate_step(input)
        for object in self.display_file:
            points = object.get_points()
            for point in points:
                point.set_y(point.get_y() - step)
        self.viewport.update()
    
    # Método de gatilho para quando objeto "Down" é apertado
    def btd_frame_down_clicked(self):
        input = int(self.txt_step.text())
        step = self.calculate_step(input)
        for object in self.display_file:
            points = object.get_points()
            for point in points:
                point.set_y(point.get_y() + step)
        self.viewport.update()
    
    # Método de gatilho para quando objeto "Right" é apertado
    def btd_frame_right_clicked(self):
        input = int(self.txt_step.text())
        step = self.calculate_step(input)
        for object in self.display_file:
            points = object.get_points()
            for point in points:
                point.set_x(point.get_x() + step)
        self.viewport.update()

    # Método de gatilho para quando objeto "Left" é apertado
    def btd_frame_left_clicked(self):
        input = int(self.txt_step.text())
        step = self.calculate_step(input)
        for object in self.display_file:
            points = object.get_points()
            for point in points:
                point.set_x(point.get_x() - step)
        self.viewport.update()
    
    # Método de gatilho para quando objeto "Left" é apertado - não funfa
    def btd_frame_out_clicked(self):
        input = int(self.txt_step.text())
        step = self.calculate_step(input)
        for object in self.display_file:
            points = object.get_points()
            for point in points:
                point.set_x(point.get_x() / step)
                point.set_y(point.get_y() / step)
        self.viewport.update()
    #(250,250),(300,350)
    # Método de gatilho para quando objeto "Left" é apertado - não funfa
    def btd_frame_in_clicked(self):
        input = float(self.txt_step.text())
        step = self.calculate_step(input)
        for object in self.display_file:
            points = object.get_points()
            for point in points:
                point.set_x(point.get_x() * step)
                point.set_y(point.get_y() * step)
        self.viewport.update()

    # Método de gatilho para quando objeto "Add object" é apertado
    def btn_add_object_clicked(self):
        self.terminal_out.append("btn_add_object_clicked clicked!!!")
        print("btn_add_object_clicked clicked")
        self.object_gui = AddObject_GUI(self)
        self.object_gui.show()

    # Método de gatilho para quando objeto "Transform object" é apertado
    def btn_transform_object_clicked(self):
        self.terminal_out.append("btn_transform_object_clicked clicked!!!")
        print("btn_transform_object_clicked clicked")
        
        self.object_gui = TransformObject_GUI(self)
        self.object_gui.show()

    # Método que objetos no display_file
    def add_object_display_file(self, object):
        self.display_file.append(object)
        self.list_objects.add_object_view(object.get_name())

    # Getter do display_file
    def get_display_file(self):
        return self.display_file


# Inicializa a Window
def window():
    app = QApplication(sys.argv)
    win = Main_GUI()
    win.show()
    sys.exit(app.exec_())

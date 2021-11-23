import os
import sys
from typing import Dict, List
from PyQt5 import uic
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import *

from src.model.point import Point
from src.view.AddObject_GUI import AddObject_GUI
from src.view.TransformObject_GUI import TransformObject_GUI
from src.view.Viewport import Viewport
from src.view.ListObject import ListObject
from src.utils.transformation import Transformation
from src.utils.wavefront import WavefrontOBJ

# Classe responsável pela interface principal de interação
class Main_GUI(QMainWindow):
    # Método construtor da interface principal
    def __init__(self):
        super(Main_GUI, self).__init__()
        self.init_ui()
        self.display_file = []
        self.new_objs = WavefrontOBJ()

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

        self.btn_horario.clicked.connect(self.btn_horario_clicked)
        self.btn_antihorario.clicked.connect(self.btn_antihorario_clicked)

        self.btn_export.clicked.connect(self.btn_export_clicked)
        self.btn_import.clicked.connect(self.open_file_dialog)

        # open_file.triggered.connect(self.open_file_dialog)


    def open_file_dialog(self):
        filename = QFileDialog().getOpenFileName()

        if filename[0] == []:
            return

        path_obj = filename[0]
        path_mtl = os.path.dirname(filename[0])

        if path_obj[-3:] != "obj":
            self.error_dialog.showMessage('Você deve selecionar um arquivo no formato .obj')
            return
        
        try:
            self.new_objs.load_obj(path_obj,path_mtl)
            self.add_new_obj_action.trigger()
            
        except FileNotFoundError:
            pass

    # Método que calcula o passo de movimentação da window
    # def calculate_step(self, input):
    #     step = (self.viewport.width * input) / 100
    #     return step

    # Método de gatilho para quando objeto "Up" é apertado    
    def btd_frame_up_clicked(self):
        input = int(self.txt_step.text())
        # step = self.calculate_step(input)
        transformation = Transformation("Transladar", 0, input)
        for object in self.display_file:
            object.apply_transformation([transformation])
        self.viewport.update()
    
    # Método de gatilho para quando objeto "Down" é apertado
    def btd_frame_down_clicked(self):
        input = int(self.txt_step.text())
        # step = self.calculate_step(input)
        transformation = Transformation("Transladar", 0, -input)
        for object in self.display_file:
            object.apply_transformation([transformation])
        self.viewport.update()
    
    # Método de gatilho para quando objeto "Right" é apertado
    def btd_frame_right_clicked(self):
        input = int(self.txt_step.text())
        # step = self.calculate_step(input)
        transformation = Transformation("Transladar", input, 0)
        for object in self.display_file:
            object.apply_transformation([transformation])
        self.viewport.update()

    # Método de gatilho para quando objeto "Left" é apertado
    def btd_frame_left_clicked(self):
        input = int(self.txt_step.text())
        # step = self.calculate_step(input)
        transformation = Transformation("Transladar", -input, 0)
        for object in self.display_file:
            object.apply_transformation([transformation])
        self.viewport.update()
    
    # Método de gatilho para quando objeto "Left" é apertado - não funfa
    def btd_frame_out_clicked(self):
        input = int(self.txt_step.text())
        # step = self.calculate_step(input)
        for object in self.display_file:
            object_center = object.get_center()
            translation_center = Transformation("Transladar", -object_center.get_x(), -object_center.get_y())
            transformation = Transformation("Escalonar", 1 / input, 1 / input)
            translation_original = Transformation("Transladar", object_center.get_x(), object_center.get_y())  
            object.apply_transformation([translation_center, transformation, translation_original])
        self.viewport.update()
    #(250,250),(300,350)

    # Método de gatilho para quando objeto "Left" é apertado - não funfa
    def btd_frame_in_clicked(self):
        input = int(self.txt_step.text())
        # step = self.calculate_step(input)
        for object in self.display_file:
            object_center = object.get_center()
            translation_center = Transformation("Transladar", -object_center.get_x(), -object_center.get_y())
            transformation = Transformation("Escalonar", input, input)
            translation_original = Transformation("Transladar", object_center.get_x(), object_center.get_y())  
            object.apply_transformation([translation_center, transformation, translation_original])
        self.viewport.update()

    # Método gatilho para a rotação da window em sentido horário
    def btn_horario_clicked(self):
        #print('horario')
        degreeAngle = float(self.txt_grau.text())
        viewport_center = self.viewport.get_center()
        #rotação
        translation_center = Transformation("Transladar", -viewport_center.get_x(), -viewport_center.get_y())
        transformation = Transformation("Rotacionar_window", viewport_center, -degreeAngle)
        translation_original = Transformation("Transladar", viewport_center.get_x(), viewport_center.get_y())
        for object in self.display_file:
            object.apply_transformation([translation_center, transformation, translation_original])
        self.viewport.update()

    # Método gatilho para a rotação da window em sentido anti-horário
    def btn_antihorario_clicked(self):
        #print('antihorario')
        degreeAngle = float(self.txt_grau.text())
        viewport_center = self.viewport.get_center()
        #rotação
        translation_center = Transformation("Transladar", -viewport_center.get_x(), -viewport_center.get_y())
        transformation = Transformation(
            "Rotacionar_window", viewport_center, degreeAngle)
        translation_original = Transformation("Transladar", viewport_center.get_x(), viewport_center.get_y())
        for object in self.display_file:
            object.apply_transformation([translation_center, transformation, translation_original])
        self.viewport.update()

    # Método de gatilho para quando objeto "Add object" é apertado
    def btn_add_object_clicked(self):
        self.terminal_out.append("btn_add_object_clicked clicked!!!")
        #print("btn_add_object_clicked clicked")
        self.object_gui = AddObject_GUI(self)
        self.object_gui.show()

    # Método de gatilho para quando objeto "Transform object" é apertado
    def btn_transform_object_clicked(self):
        self.terminal_out.append("btn_transform_object_clicked clicked!!!")
        #print("btn_transform_object_clicked clicked")
        
        self.object_gui = TransformObject_GUI(self)
        self.object_gui.show()

    # Método que objetos no display_file
    def add_object_display_file(self, object):
        self.display_file.append(object)
        self.list_objects.add_object_view(object.get_name())
    
    # Método que objetos no display_file
    def btn_import_clicked(self):
        print('btn import clicked!!')


    # Método que objetos no display_file
    def btn_export_clicked(self):
        print('btn export clicked!!')

    # Getter do display_file
    def get_display_file(self):
        return self.display_file

    def import_handler(self):
        objs : Dict[str, List[Point]]= self.main_window.new_objs
        i = 0

        
        for key, value in objs.objects.items():

            if objs.mtls:
                usemtl = objs.usemtl[i]
                newmtl = objs.new_mtl.index(usemtl)

                rgb = [round(int(float(i) * 255)) for i in objs.kd_params[newmtl]] 
            else:
                rgb = [0,0,0] 

            if len(value) == 1:
                self.add_new_object(key, value, "PONTO", QColor(rgb[0],rgb[1],rgb[2]),objs.filled[i]) 
            elif len(value) == 2:
                self.add_new_object(key, value, "LINHA", QColor(rgb[0],rgb[1],rgb[2]), objs.filled[i])
            else:
                self.add_new_object(key, value, "POLIGONO", QColor(rgb[0],rgb[1],rgb[2]), objs.filled[i])
            i += 1
    
        if objs.faces:
            rgb = [0,0,0]

            self.add_new_object("Wavefront_obj_3D", objs.vertices, Point, QColor(rgb[0],rgb[1],rgb[2]), edges = objs.edges, faces = objs.faces, from_wavefront=True)      

        if objs.window:
            coords = []
            for c in objs.window:
                coords.append([c.x(),c.y(),c.z()])
            self.update_window_values(coords)

        self.calculate_scn_coordinates()



# Inicializa a Window
def window():
    app = QApplication(sys.argv)
    win = Main_GUI()
    win.show()
    sys.exit(app.exec_())


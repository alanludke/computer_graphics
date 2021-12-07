import os
import sys
from typing import Dict, List
from PyQt5 import uic
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import *

from src.model.window import Window
from src.model.line import Line
from src.model.polygon import Polygon
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
        self.display_window = Window([250, 250], 500, 500)

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

        self.add_new_obj_action = QAction('Adicionar novos objetos', self)
        self.add_new_obj_action.triggered.connect(lambda: self.import_handler())

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
            print("Nenhum arquivo com esse nome foi encontrado!")

    # Método de gatilho para quando objeto "Up" é apertado    
    def btd_frame_up_clicked(self):
        input = self.txt_step.text()
        transformation = None
        if(input == ""):
            transformation = Transformation("Transladar", 0, 10)
        else:
            step = int(input)
            transformation = Transformation("Transladar", 0, step)
        
        for object in self.display_file:
            object.apply_transformation([transformation])
            object.set_normalized_coords(self.display_window)
        self.viewport.update()
    
    # Método de gatilho para quando objeto "Down" é apertado
    def btd_frame_down_clicked(self):
        input = self.txt_step.text()
        transformation = None
        if(input == ""):
            transformation = Transformation("Transladar", 0, -10)
        else:
            step = int(input)
            transformation = Transformation("Transladar", 0, -step)
        for object in self.display_file:
            object.apply_transformation([transformation])
            object.set_normalized_coords(self.display_window)
        self.viewport.update()
    
    # Método de gatilho para quando objeto "Right" é apertado
    def btd_frame_right_clicked(self):
        input = self.txt_step.text()
        transformation = None
        if(input == ""):
            transformation = Transformation("Transladar", -10, 0)
        else:
            step = int(input)
            transformation = Transformation("Transladar", -step, 0)
        for object in self.display_file:
            object.apply_transformation([transformation])
            object.set_normalized_coords(self.display_window)
        self.viewport.update()

    # Método de gatilho para quando objeto "Left" é apertado
    def btd_frame_left_clicked(self):
        input = self.txt_step.text()
        transformation = None
        if(input == ""):
            transformation = Transformation("Transladar", 10, 0)
        else:
            step = int(input)
            transformation = Transformation("Transladar", step, 0)
        for object in self.display_file:
            object.apply_transformation([transformation])
            object.set_normalized_coords(self.display_window)
        self.viewport.update()
    
    # Método de gatilho para quando objeto "Left" é apertado - não funfa
    def btd_frame_out_clicked(self):
        input = self.txt_step.text()
        if(input == ""):
            for object in self.display_file:
                object_center = object.get_center()
                translation_center = Transformation("Transladar", -object_center.get_x(), -object_center.get_y())
                transformation = Transformation("Escalonar", 1 / 10, 1 / 10)
                translation_original = Transformation("Transladar", object_center.get_x(), object_center.get_y())  
                object.apply_transformation([translation_center, transformation, translation_original])
                object.set_normalized_coords(self.display_window)
        else:
            step = int(input)
            for object in self.display_file:
                object_center = object.get_center()
                translation_center = Transformation("Transladar", -object_center.get_x(), -object_center.get_y())
                transformation = Transformation("Escalonar", 1 / step, 1 / step)
                translation_original = Transformation("Transladar", object_center.get_x(), object_center.get_y())  
                object.apply_transformation([translation_center, transformation, translation_original])
                object.set_normalized_coords(self.display_window)
        self.viewport.update()

    # Método de gatilho para quando objeto "Left" é apertado - não funfa
    def btd_frame_in_clicked(self):
        input = self.txt_step.text()
        if(input == ""):
            for object in self.display_file:
                object_center = object.get_center()
                translation_center = Transformation("Transladar", -object_center.get_x(), -object_center.get_y())
                transformation = Transformation("Escalonar", 10, 10)
                translation_original = Transformation("Transladar", object_center.get_x(), object_center.get_y())  
                object.apply_transformation([translation_center, transformation, translation_original])
                object.set_normalized_coords(self.display_window)
        else:
            step = int(input)
            for object in self.display_file:
                object_center = object.get_center()
                translation_center = Transformation("Transladar", -object_center.get_x(), -object_center.get_y())
                transformation = Transformation("Escalonar", step, step)
                translation_original = Transformation("Transladar", object_center.get_x(), object_center.get_y())  
                object.apply_transformation([translation_center, transformation, translation_original])
                object.set_normalized_coords(self.display_window)
        self.viewport.update()

    # Método gatilho para a rotação da window em sentido horário
    def btn_horario_clicked(self):
        degreeAngle = float(self.txt_grau.text())
        viewport_center = self.viewport.get_center()
        #rotação
        translation_center = Transformation("Transladar", -viewport_center.get_x(), -viewport_center.get_y())
        transformation = Transformation("Rotacionar_window", viewport_center, -degreeAngle)
        translation_original = Transformation("Transladar", viewport_center.get_x(), viewport_center.get_y())
        for object in self.display_file:
            object.apply_transformation([translation_center, transformation, translation_original])
            object.set_normalized_coords(self.display_window)
        self.viewport.update()

    # Método gatilho para a rotação da window em sentido anti-horário
    def btn_antihorario_clicked(self):
        degreeAngle = float(self.txt_grau.text())
        viewport_center = self.viewport.get_center()
        #rotação
        translation_center = Transformation("Transladar", -viewport_center.get_x(), -viewport_center.get_y())
        transformation = Transformation(
            "Rotacionar_window", viewport_center, degreeAngle)
        translation_original = Transformation("Transladar", viewport_center.get_x(), viewport_center.get_y())
        for object in self.display_file:
            object.apply_transformation([translation_center, transformation, translation_original])
            object.set_normalized_coords(self.display_window)
        self.viewport.update()

    # Método de gatilho para quando objeto "Add object" é apertado
    def btn_add_object_clicked(self):
        self.terminal_out.append("btn_add_object_clicked clicked!!!")
        self.object_gui = AddObject_GUI(self)
        self.object_gui.show()

    # Método de gatilho para quando objeto "Transform object" é apertado
    def btn_transform_object_clicked(self):
        self.terminal_out.append("btn_transform_object_clicked clicked!!!")
        
        self.object_gui = TransformObject_GUI(self)
        self.object_gui.show()

    # Método que objetos no display_file
    def add_object_display_file(self, object):
        self.display_file.append(object)
        self.list_objects.add_object_view(object.get_name())
    
    # Método que exporta objetos do display_file para arquivo obj
    def btn_export_clicked(self):
        print('btn export clicked!!')
        self.new_objs.export_obj(self.display_file, self.display_window)

    # Getter do display_file
    def get_display_file(self):
        return self.display_file

    ## Método que importa objetos, de arquivo obj, no display_file
    def import_handler(self): 
        objs : Dict[str, List[Point]]= self.new_objs
        i = 0
        for key, value in objs.objects.items():
            if objs.mtls:
                usemtl = objs.usemtl[i]
                newmtl = objs.new_mtl.index(usemtl)
                rgb = [round(int(float(i) * 255)) for i in objs.kd_params[newmtl]]
                color = QColor(rgb[0], rgb[1], rgb[2])
            else:
                color = QColor(0, 0, 0)
            self.add_new_object(key, value, color)
            i += 1
        self.display_window = Window( [objs.window[0].get_x(), objs.window[0].get_y()] , objs.window[1].get_x(), objs.window[1].get_y())
        # self.centralize_window()
        self.viewport.draw_objects(self.display_file)
        self.terminal_out.append("btn_add clicked!!!")

    # Adiciona novos objetos, importados de arquivo obj
    def add_new_object(self, name, coord, color):
        object = None
        if coord[0] == 'p':
            object = Point(name, coord[1].get_x(), coord[1].get_y(), 1)
            object.set_color(color)
        elif coord[0] == 'l':
            coord.pop(0)
            object = Line(name, coord)
            object.set_color(color)
        elif coord[0] == 'f':
            coord.pop(0)
            object = Polygon(name, coord)
            object.set_color(color)
        
        if object != None:
            object.set_normalized_coords(self.display_window)    
            self.add_object_display_file(object)
            # for pt in object.get_points():
            #     print(f'pt ({pt.get_x()}, {pt.get_y()})')
            # for pt in object.get_normalized_points():
            #     print(f'pn ({pt.get_x()}, {pt.get_y()})')

        # self.viewport.draw_objects(self.display_file)    

    def centralize_window(self):
        w_center = self.display_window.get_center()
        transformation = Transformation("Transladar", -w_center.get_x(), -w_center.get_y())
        for object in self.display_file:
            object.apply_transformation([transformation])
            object.set_normalized_coords(self.display_window)
        
        self.viewport.update()
    
# Inicializa a Main_GUI
def window():
    app = QApplication(sys.argv)
    win = Main_GUI()
    win.show()
    sys.exit(app.exec_())


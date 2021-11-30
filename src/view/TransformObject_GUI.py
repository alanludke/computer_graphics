import sys
from PyQt5 import uic
from PyQt5.QtCore import QTextEncoder
from PyQt5.QtWidgets import *
from src.model.point import Point
from src.model.polygon import Polygon
from src.model.line import Line
from src.view.ListTransformations import ListTransformation
from src.utils.transformation import Transformation

# Classe responsável pelo Frame onde são criados os objetos
class TransformObject_GUI(QDialog):

    # Método construtor
    def __init__(self, parent):
        super(TransformObject_GUI, self).__init__(parent)
        self.init_ui()
        self.parent = parent
        self.selected_object = parent.list_objects.selectedItems()[0]
        self.display_file_transformations = []

    # Inicializa componentes da interface, layouts e botões
    def init_ui(self):
        uic.loadUi("src/view/transform_object_gui.ui", self)

        # Lista de objetos
        self.list_transformations = ListTransformation(self)
        self.layout_list_transformations.addWidget(self.list_transformations)
        self.txt_point.setPlaceholderText("(x,y)")

        # buttons
        self.btn_add_transformation.clicked.connect(self.btn_transform_object_clicked)
        self.btn_add_rotacao.clicked.connect(self.btn_add_rotacao_clicked)
        self.btn_apply_transformations.clicked.connect(
            self.btn_apply_transformations_clicked
        )
        self.btn_clear_list_transformation.clicked.connect(self.clear_list_trasnformation)

    # Método de gatilho para quando objeto "Transform object(Escalonar/Transladar)" é apertado
    def btn_transform_object_clicked(self):
        object = self.create_transformation()
        for transformation in object:
            self.add_object_display_file(transformation)

        self.parent.terminal_out.append("btn_transform_object clicked!!!")

    # Método de gatilho para quando objeto "Transform object(Escalonar/Transladar)" é apertado
    def btn_add_rotacao_clicked(self):
        object = self.create_transformation()
        for transformation in object:
            self.add_object_display_file(transformation)

        self.parent.terminal_out.append("btn_add_rotacao_clicked clicked!!!")

    # Método de gatilho para quando objeto "Transform object(Escalonar/Transladar)" é apertado
    def btn_apply_transformations_clicked(self):
        object_name = self.selected_object.text()
        object = self.get_selected_object(object_name)

        object.apply_transformation(self.display_file_transformations)
        object.set_normalized_coords(self.parent.display_window)
        self.parent.viewport.draw_objects(self.parent.get_display_file())
        self.parent.terminal_out.append("btn_apply_transformations_clicked clicked!!!")

    # Método que limpa a lista de transformações a serem aplicadas
    def clear_list_trasnformation(self):
        self.list_transformations.clear()
        self.display_file_transformations.clear()

    # Método que objetos nodisplay_file_transformations
    def add_object_display_file(self, transformation):
        self.display_file_transformations.append(transformation)
        self.list_transformations.add_transform_object_view(
            f"Ação de {transformation.action}"
        )

    # Método responsável por criar uma transformacao dependendo de seu tipo
    def create_transformation(self):
        transformation = None

        if self.rbtn_escalonar.isChecked():
            if(self.txt_coord_x.toPlainText() == ''):
                coord_x = 1
                coord_y = float(self.txt_coord_y.toPlainText())
            elif(self.txt_coord_y.toPlainText() == ''):
                coord_x = float(self.txt_coord_x.toPlainText())
                coord_y = 1
            else:
                coord_x = float(self.txt_coord_x.toPlainText())
                coord_y = float(self.txt_coord_y.toPlainText())
            coord_z = 1
            
            object_name = self.selected_object.text()
            object_center = self.get_selected_object(object_name).get_center()
            
            translation_center = Transformation("Transladar", -object_center.get_x(), -object_center.get_y())
            transformation = Transformation("Escalonar", coord_x, coord_y)
            translation_original = Transformation("Transladar", object_center.get_x(), object_center.get_y())
            
            return [translation_center, transformation, translation_original]

        elif self.btn_transladar.isChecked():
            if(self.txt_coord_x.toPlainText() == ''):
                coord_x = 0
                coord_y = float(self.txt_coord_y.toPlainText())
            elif(self.txt_coord_y.toPlainText() == ''):
                coord_x = float(self.txt_coord_x.toPlainText())
                coord_y = 0
            else:
                coord_x = float(self.txt_coord_x.toPlainText())
                coord_y = float(self.txt_coord_y.toPlainText())
            coord_z = 1
            transformation = Transformation("Transladar", coord_x, coord_y)
            
            return [transformation]

        elif self.rbtn_rotacao_centro_mundo.isChecked():
            point = Point("centro", 0, 0, 1)
            angle = float(self.txt_angulo_rotacao.toPlainText())

            transformation = Transformation("Rotacionar_centro_mundo", point, angle)

            return [transformation]
            
        elif self.rbtn_rotacao_centro_objeto.isChecked():
            object_name = self.selected_object.text()
            object_center = self.get_selected_object(object_name).get_center()
            angle = float(self.txt_angulo_rotacao.toPlainText())

            translation_center = Transformation("Transladar", -object_center.get_x(), -object_center.get_y())
            transformation = Transformation(
                "Rotacionar_centro_objeto", object_center, angle
            )
            translation_original = Transformation("Transladar", object_center.get_x(), object_center.get_y())

            return [translation_center, transformation, translation_original]

        elif self.rbtn_rotacao_ponto.isChecked():
            raw_point = self.txt_point.toPlainText().split(",")
            point = Point(
                "centro",
                int(raw_point[0].replace("(", "")),
                int(raw_point[-1].replace(")", "")),
                1,
            )
            angle = float(self.txt_angulo_rotacao.toPlainText())

            translation_center = Transformation("Transladar", -point.get_x(), -point.get_y())
            transformation = Transformation("Rotacionar_centro_objeto", point, angle)
            translation_original = Transformation("Transladar", point.get_x(), point.get_y())

            return [translation_center, transformation, translation_original]
        else:
            print(f"nenhum tipo de rotação marcado!")

    def get_selected_object(self, object_name):
        for each in self.parent.get_display_file():
            if each.get_name() == object_name:
                return each

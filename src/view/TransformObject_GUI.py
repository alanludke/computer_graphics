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
        self.initUI()
        self.parent = parent
        self.selected_object = parent.list_objects.selectedItems()[0]
        self.display_file = []

    # Inicializa componentes da interface, layouts e botões
    def initUI(self):
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

    # Método de gatilho para quando objeto "Transform object(Escalonar/Transladar)" é apertado
    def btn_transform_object_clicked(self):
        object = self.createTransformation()

        self.transformObjectDisplayFile(object)
        self.parent.terminal_out.append("btn_transform_object clicked!!!")

        print("btn_transform_object clicked")

    # Método de gatilho para quando objeto "Transform object(Escalonar/Transladar)" é apertado
    def btn_add_rotacao_clicked(self):
        object = self.createTransformation()

        self.transformObjectDisplayFile(object)
        self.parent.terminal_out.append("btn_add_rotacao_clicked clicked!!!")

        print("btn_transform_object clicked")

    # pegar o objeto
    # pegar a lista de objetos transformações
    # gerar uma lista com as matrizes as transformações
    # chamar um metodo apply_transformation() do objeto
    # 
    def btn_apply_transformations_clicked(self):
        object_name = self.selected_object.text()
        object = self.getSelectedObject(object_name)

        object.apply_transformation()
        self.parent.terminal_out.append("btn_apply_transformations_clicked clicked!!!")


    # Método que objetos no display_file
    def transformObjectDisplayFile(self, transformation):
        self.display_file.append(transformation)
        self.list_transformations.add_transform_object_view(
            f"Ação de {transformation.action}"
        )

    # Método responsável por criar uma transformacao dependendo de seu tipo
    def createTransformation(self):
        transformation = None

        if self.rbtn_escalonar.isChecked():
            print(f"rbtn_escalonar marcado!")
            coord_x = float(self.txt_coord_x.toPlainText())
            coord_y = float(self.txt_coord_y.toPlainText())
            coord_z = 1
            transformation = Transformation("Escalonar", coord_x, coord_y)
        elif self.btn_transladar.isChecked():
            print(f"btn_transladar marcado!")
            coord_x = float(self.txt_coord_x.toPlainText())
            coord_y = float(self.txt_coord_y.toPlainText())
            coord_z = 1
            transformation = Transformation("Transladar", coord_x, coord_y)
        elif self.rbtn_rotacao_centro_mundo.isChecked():
            print(f"rbtn_rotacao_centro_mundo marcado!")
            point = Point("centro", 0, 0, 1)
            angle = float(self.txt_angulo_rotacao.toPlainText())
            transformation = Transformation("Rotacionar_centro_mundo", point, angle)
        elif self.rbtn_rotacao_centro_objeto.isChecked():
            print(f"rbtn_rotacao_centro_objeto marcado!")

            object_name = self.selected_object.text()
            object_center = self.getSelectedObject(object_name).getCenter()
            angle = float(self.txt_angulo_rotacao.toPlainText())
            transformation = Transformation(
                "Rotacionar_centro_objeto", object_center, angle
            )
        elif self.rbtn_rotacao_ponto.isChecked():
            print(f"rbtn_rotacao_ponto marcado!")
            raw_point = self.txt_point.toPlainText().split(",")
            point = Point(
                "centro",
                int(raw_point[0].replace("(", "")),
                int(raw_point[-1].replace(")", "")),
                1,
            )
            angle = float(self.txt_angulo_rotacao.toPlainText())
            transformation = Transformation("Rotacionar_centro_objeto", point, angle)
        else:
            print(f"nenhum marcado!")
        return transformation

    def getSelectedObject(self, object_name):
        for each in self.parent.getDisplayFile():
            if each.getName() == object_name:
                return each
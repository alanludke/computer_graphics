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
        self.initUI()
        self.display_file = []

    # Inicializa componentes da interface, layouts e botões
    def initUI(self):
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
        # selected_item = self.list_objects.selectedItems()
        # print(f'type(selected_item) = {type(selected_item)}')
        # print(f'selected_item = {selected_item[0]}')
        self.object_gui = TransformObject_GUI(self)
        self.object_gui.show()

    # Método que objetos no display_file
    def addObjectDisplayFile(self, object):
        self.display_file.append(object)
        self.list_objects.add_object_view(object.getName())

    # Getter do display_file
    def getDisplayFile(self):
        return self.display_file

# Inicializa a Window
def window():
    app = QApplication(sys.argv)
    win = Main_GUI()
    win.show()
    sys.exit(app.exec_())

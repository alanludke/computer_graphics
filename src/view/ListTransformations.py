import sys
from PyQt5.QtWidgets import QListWidget, QListWidgetItem

# Classe responsável pela QListWidget que lista todos os objetos desenhados
class ListTransformation(QListWidget):
    # Método construtor
    def __init__(self, parent):
        super(ListTransformation, self).__init__(parent)
        self.parent = parent
        self.list_transformations = []

    # Adiciona um ObjectListItem no ListTransformation
    def add_transform_object_view(self, name_object):
        QListWidgetItem(name_object, self)
        self.list_transformations.append(name_object)

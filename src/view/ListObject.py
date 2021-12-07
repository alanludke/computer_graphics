import sys
from PyQt5.QtWidgets import QListWidget, QListWidgetItem

# Classe responsável pela QListWidget que lista todos os objetos desenhados
class ListObject(QListWidget):
    # Método construtor
    def __init__(self, parent):
        super(ListObject, self).__init__(parent)
        self.parent = parent
        self.list_objects = []

    # Adiciona um ObjectListItem no ListObject
    def add_object_view(self, name_object):
        QListWidgetItem(name_object, self)
        self.list_objects.append(name_object)

import sys
from PyQt5.QtWidgets import QListWidget, QListWidgetItem

class ListObject(QListWidget):

    def __init__(self,parent):
        super(ListObject, self).__init__(parent)
        self.parent = parent
        self.list_objects = []

    def add_object_view(self, name_object):
        QListWidgetItem(name_object, self)
        self.list_objects.append(name_object)
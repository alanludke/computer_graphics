from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QFileDialog
from typing import List
from src.model.point import Point
import os.path


class WavefrontOBJ:
    def __init__(self):
        self.path = None
        self.mtllibs = []
        self.mtls = False
        self.vertices = []
        self.window = []
        self.objects_name = []
        self.usemtl = []
        self.new_mtl = []
        self.kd_params = []
        self.objects = {}
        self.filled = []
        self.faces = []
        self.edges = []

    def parse_mtl(self, filename_mtl):
        if not os.path.exists(filename_mtl):
            self.mtls = False
            return

        with open(filename_mtl, "r") as objm:
            for line in objm:
                toks = line.split()
                if not toks:
                    continue
                if toks[0] == "newmtl":
                    self.new_mtl.append(toks[1])
                elif toks[0] == "Kd":
                    self.kd_params.append(toks[1:])

    def load_obj(self, filename_obj: str, filename_mtl: str):
        with open(filename_obj, "r") as objf:
            self.path = filename_obj

            for line in objf:
                toks = line.split()
                if not toks:
                    continue
                if toks[0] == "mtllib":
                    self.mtls = True
                    filename_mtl += f"/{toks[1]}"
                    self.parse_mtl(filename_mtl)

                # Vértice
                if toks[0] == "v":
                    t = []
                    for v in toks[1:]:
                        if "-" in v:
                            t.append(float(v.replace("\U00002013", "-")))
                        else:
                            t.append(float(v))
                    self.vertices.append(Point("vertice", t[0], t[1], 1))

                # Object
                elif toks[0] == "o":
                    self.objects_name.append(toks[1])

                # Point
                elif toks[0] == "p":

                    self.objects[self.objects_name[-1]] = [
                        self.vertices[int(toks[1]) - 1]
                    ]
                    self.filled.append(False)

                # Window
                elif toks[0] == "w":
                    indices = [float(v) - 1 for v in toks[1:]]
                    for i in indices:
                        self.window.append(self.vertices[int(i)])

                # Line
                elif toks[0] == "l":
                    indices = [float(v) - 1 for v in toks[1:]]
                    indices.append(indices[0])
                    temp = []
                    for i in indices:
                        temp.append(self.vertices[int(i)])
                    self.objects[self.objects_name[-1]] = temp
                    self.filled.append(False)

                elif toks[0] == "usemtl":
                    self.usemtl.append(toks[1])

    def export_obj(self, objects_list, window):
        try:
            points = []
            colors_list = []
            filename = QFileDialog.getSaveFileName()
            if filename[0] == "":
                return
            url = QUrl.fromLocalFile(filename[0])
            with open(filename[0] + ".obj", "w") as file:
                for obj in objects_list:
                    for pt in obj.get_points():
                        # escrevendo os vertices
                        file.write(f"v {pt.get_x()} {pt.get_y()}\n")
                        points.append(pt)

                # escrevendo infos da window
                w_center = window.get_center()
                w_dimension = Point("Dimension", window.width, window.height, 1)
                file.write(f"v {w_center.get_x()} {w_center.get_y()}\n")
                file.write(f"v {w_dimension.get_x()} {w_dimension.get_y()}\n")
                points.append(w_center)
                points.append(w_dimension)

                file.write(f"mtllib {url.fileName()}.mtl\n")
                file.write("o window\n")
                file.write(
                    f"w {points.index(w_center) + 1} {points.index(w_dimension) + 1}\n"
                )

                # escrevendo os objetos
                for obj in objects_list:
                    # Nome
                    file.write(f"o {obj.get_name()}\n")

                    # Cor
                    if obj.get_color() not in colors_list:
                        colors_list.append(obj.get_color())
                    file.write(f"usemtl color{colors_list.index(obj.get_color())}\n")

                    # Tipo
                    if obj.get_type() == "point":
                        for pt in obj.get_points():
                            file.write(f"p {points.index(pt) + 1}\n")
                    elif obj.get_type() == "line":
                        text_line = ""
                        for pt in obj.get_points():
                            text_line += f"{points.index(pt) + 1} "
                        file.write(f"l {text_line}\n")
                    elif obj.get_type() == "polygon":
                        text_line = ""
                        for pt in obj.get_points():
                            text_line += f"{points.index(pt) + 1} "
                        file.write(f"f {text_line}\n")

            # escreve arquivo mtl
            with open(filename[0] + ".mtl", "w") as file:
                for c in colors_list:
                    file.write(f"newmtl color{colors_list.index(c)}\n")
                    color = c.redF()
                    file.write(f"Kd {c.redF()} {c.greenF()} {c.blueF()}" "\n")

        except:
            print("Não foi possível exportar o arquivo!")

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from decimal import Decimal
import sys
import math

class Janela(QWidget):
    __mainLayout = QHBoxLayout()
    __entradaFaixa = 0
    __listaObjetos = 0
    __pontosW = []
    __pontosV = []
    __Wc = [] # Centro da window
    __zoom = 0
    __viewport = 0
    __menuF = 0
    __objetos = []
    __objetoAnteriorTransformacao = []

    def __init__(self, parent=None):
        super(Janela, self).__init__()
        self.__menuF = self.__menuFuncoes()
        self.setWindowTitle("Computação Gráfica")
        self.resize(800, 600)
        self.setLayout(self.__mainLayout)
        self.__centralizar()
        self.__painelViewport()
        self.__lista()
        self.__window()

    def __menuFuncoes(self):
        layout = QVBoxLayout()
        painel = QFrame()
        painel.setMaximumWidth(self.width()*(0.4))
        painel.setLayout(layout)
        layoutMenuFuncoes = QVBoxLayout()
        grupo = QGroupBox()
        grupo.setTitle("Menu de Funções")
        grupo.setLayout(layoutMenuFuncoes)
        layout.addWidget(grupo)
        self.__mainLayout.addWidget(painel)
        return layoutMenuFuncoes

    def contextMenuEvent(self, event):
        menu = QMenu(self)
        menu.addAction("Adicionar Polígono", lambda: self.__addPoligono())
        menu.addAction("Adicionar Reta", lambda: self.__addReta())
        menu.addAction("Adicionar Ponto", lambda: self.__addPonto())
        menu.exec_(self.mapToGlobal(event.pos()))

    def __lista(self):
        self.__listaObjetos = QListWidget()
        self.__listaObjetos.setMinimumWidth(900)
        layout = QVBoxLayout()
        grupo = QGroupBox()
        grupo.setTitle("Objetos")
        grupo.setLayout(layout)
        layout.addWidget(self.__listaObjetos)
        self.__menuF.addWidget(grupo)

    def __window(self):
        layout = QVBoxLayout()
        grupo = QGroupBox()
        grupo.setTitle("Window")
        grupo.setLayout(layout)
        layoutPainel = QGridLayout()
        painel = QFrame()
        painel.setLayout(layoutPainel)
        botaoIn = QPushButton("In")
        botaoIn.clicked.connect(lambda: self.__zoomIn())
        botaoOut = QPushButton("Out")
        botaoOut.clicked.connect(lambda: self.__zoomOut())
        botaoUp = QPushButton("Up")
        botaoUp.clicked.connect(lambda: self.__up())
        botaoLeft = QPushButton("Left")
        botaoLeft.clicked.connect(lambda: self.__left())
        botaoRight = QPushButton("Right")
        botaoRight.clicked.connect(lambda: self.__right())
        botaoDown = QPushButton("Down")
        botaoDown.clicked.connect(lambda: self.__down())
        layoutPainel.addWidget(QLabel("Faixa"), 0, 0)
        self.__entradaFaixa = QLineEdit()
        self.__entradaFaixa.setReadOnly(True)
        layoutPainel.addWidget(self.__entradaFaixa, 0, 1, 1, 3)
        self.__entradaFaixa.setText(str(self.__zoom))
        layoutPainel.addWidget(QLabel("%"), 0, 4)
        layoutPainel.addWidget(botaoIn, 1, 3)
        layoutPainel.addWidget(botaoOut, 3, 3)
        layoutPainel.addWidget(botaoUp, 1, 1)
        layoutPainel.addWidget(botaoLeft, 2, 0)
        layoutPainel.addWidget(botaoRight, 2, 2)
        layoutPainel.addWidget(botaoDown, 3, 1)
        layout.addWidget(painel)
        self.__menuF.addWidget(grupo)

        #Interface das funções de transformação de objetos
        layout = QVBoxLayout()
        grupo = QGroupBox()
        grupo.setTitle("Rotação")
        grupo.setLayout(layout)
        layoutTransf = QGridLayout()
        painel = QFrame()
        painel.setLayout(layoutTransf)
        botaoCentroMundo = QPushButton("Centro Mundo")
        #botaoIn.clicked.connect(lambda: self.__zoomIn())
        botaoCentroObjeto = QPushButton("Centro Objeto")
        #botaoIn.clicked.connect(lambda: self.__zoomIn())
        botaoArbitrario = QPushButton("Ponto Arbitrário")
        #botaoIn.clicked.connect(lambda: self.__zoomIn())
        botaoZoomIN = QPushButton("+")
        #botaoIn.clicked.connect(lambda: self.__Escalonamento(1,5))
        botaoZoomOUT = QPushButton("-")
        #botaoIn.clicked.connect(lambda: self.__Escalonamento(-1,5))
        botaoTranslacao = QPushButton("Translação")
        #botaoIn.clicked.connect(lambda: self.__zoomIn())
        layoutTransf.addWidget(QLabel("Graus"), 0, 0)
        self.__entradaGraus = QLineEdit()
        self.__entradaGraus.setReadOnly(True)
        
        layoutTransf.addWidget(self.__entradaGraus, 0, 1, 1, 3)
        layoutTransf.addWidget(botaoCentroMundo, 1, 1)
        layoutTransf.addWidget(botaoCentroObjeto, 2, 1)
        layoutTransf.addWidget(botaoArbitrario, 3, 1)
        layoutTransf.addWidget(botaoTranslacao, 1, 2)
        layoutTransf.addWidget(QLabel("Zoom"), 4, 0)
        layoutTransf.addWidget(botaoZoomIN, 4, 1)
        layoutTransf.addWidget(botaoZoomOUT, 4, 2)
        layout.addWidget(painel)
    
        self.__menuF.addWidget(grupo)

    def __painelViewport(self):
        layout = QVBoxLayout()
        painel = QFrame()
        painel.setLayout(layout)
        self.__viewport = QGraphicsView()
        self.__viewport.setScene(QGraphicsScene())
        layoutStatus = QVBoxLayout()
        status = QFrame()
        status.setLayout(layoutStatus)
        layoutStatus.addWidget(QLabel("Para adicionar uma forma, clique com o botão direito do mouse em qualquer área da tela e selecione uma opção."))
        vp = QLabel("Viewport")
        vp.setStyleSheet("font-weight: bold;")
        layout.addWidget(vp)
        layout.addWidget(self.__viewport, 20)
        layout.addWidget(status, 1)
        self.__mainLayout.addWidget(painel)
        # self.__pontosW = [(-1*self.width()), (-1*self.height()), self.width(), self.height()]
        self.__pontosW = [0, 0, self.__viewport.width(), self.__viewport.height()]
        self.__pontosV = [0, 0, self.__viewport.width(), self.__viewport.height()]
        self.__Wc = [self.width()/2, self.height()/2]

    def __centralizar(self):
        geometriaJanela = self.frameGeometry()
        geometriaTela = QDesktopWidget().availableGeometry().center()
        geometriaJanela.moveCenter(geometriaTela)
        self.move(geometriaJanela.topLeft())

    def __zoomIn(self):
        self.__pontosW[2] += 100
        self.__pontosW[3] += 100
        self.__zoom += 10
        self.__entradaFaixa.setText(str(self.__zoom))
        self.__atualziarViewport()

    def __zoomOut(self):
        self.__pontosW[2] -= 100
        self.__pontosW[3] -= 100
        self.__zoom -= 10
        self.__entradaFaixa.setText(str(self.__zoom))
        self.__atualziarViewport()

    def __up(self):
        self.__pontosW[1] -= 100
        self.__pontosW[3] -= 100
        self.__atualziarViewport()

    def __right(self):
        self.__pontosW[0] -= 100
        self.__pontosW[2] -= 100
        self.__atualziarViewport()

    def __left(self):
        self.__pontosW[0] += 100
        self.__pontosW[2] += 100
        self.__atualziarViewport()

    def __down(self):
        self.__pontosW[1] += 100
        self.__pontosW[3] += 100
        self.__atualziarViewport()

    def __transformadaDeViewport(self, xw, yw):
        xwmin = self.__pontosW[0]
        ywmin = self.__pontosW[1]
        xwmax = self.__pontosW[2]
        ywmax = self.__pontosW[3]
        xvmin = self.__pontosV[0]
        yvmin = self.__pontosV[1]
        xvmax = self.__pontosV[2]
        yvmax = self.__pontosV[3]
        xv = ((xw-xwmin)/(xwmax-xwmin))*(xvmax-xvmin)
        yv = (1-((yw-ywmin)/(ywmax-ywmin)))*(yvmax-yvmin)
        return [xv, yv]

    

    def __addObjeto(self, iObj):
        if iObj.isVisible() == False:
            if iObj.getObjeto() != 0:
                self.__objetos.append(iObj.getObjeto())
                self.__atualizarLista()
                self.__atualziarViewport()

    def __renderizar(self, tipo, pontosViewport):
        if tipo == 0:
            poligono = QPolygonF(pontosViewport) # infinitos pontos
            self.__viewport.scene().addPolygon(poligono, QPen(QColor(0, 0, 0), 1, Qt.SolidLine), QBrush(Qt.NoBrush))
        elif tipo == 1:
            reta = QLineF(pontosViewport[0], pontosViewport[1]) # dois pontos
            self.__viewport.scene().addLine(reta, QPen(QColor(0, 0, 0), 1, Qt.SolidLine))
        elif tipo == 2:
            ponto = QLineF(pontosViewport[0], pontosViewport[1], pontosViewport[0], pontosViewport[1]) # um ponto
            self.__viewport.scene().addLine(ponto, QPen(QColor(0, 0, 0), 3, Qt.SolidLine))

    def __atualziarViewport(self):
        self.__viewport.viewport().update()
        self.__viewport.scene().clear()
        for objeto in self.__objetos:
            pontos = []
            for i in range(0, len(objeto.getPontos())):
                if i % 2 != 0:
                    coordenadas = self.__transformadaDeViewport(objeto.getPontos()[i-1], objeto.getPontos()[i])
                    if objeto.getTipo() == 2:
                        pontos.append(coordenadas[0])
                        pontos.append(coordenadas[1])
                    else:
                        pontos.append(QPointF(coordenadas[0], coordenadas[1]))
                    i+1
            self.__renderizar(objeto.getTipo(), pontos)

    def __atualizarLista(self):
        self.__listaObjetos.clear()
        for objeto in self.__objetos:
            if objeto.getTipo() == 0:
                nome = objeto.getNome()+": Polígono"
            elif objeto.getTipo() == 1:
                nome = objeto.getNome()+": Reta"
            elif objeto.getTipo() == 2:
                nome = objeto.getNome()+": Ponto"
            self.__listaObjetos.addItem(nome)

    #def _TransCoordenadasHomogeneas(self, objeto):

    #def __getNovaPosicao(self):
    def __Transladar(self, pontos, deslocamento):
        novaPosicao = [] 
        j = 0
        for j in pontos:
            novaPosicao[j] = pontos[j] + deslocamento[j]
        return novaPosicao

    def __Translacao(self, objeto, novosPontos):
        pontos = objeto.getPontos()
        tipo = objeto.getTipo()
        deslocamento = []
        i = 0
        for i in novosPontos:
            deslocamento[i] = novosPontos[i] - pontos[i]
        novaPosicao = self.__Transladar(pontos, deslocamento)
        self.__renderizar(tipo, novaPosicao)

    def __Escalonamento(self, objeto, zoom):
        pontos = objeto.getPontos()
        tipo = objeto.getTipo()
        novaPosicao = []
        i = 0
        for i in pontos:
            novaPosicao[i] = pontos[i] * zoom
        self.__renderizar(tipo, novaPosicao)

    #centro mundo, centro objeto, arbitrário
    def __RotacaoCentroMundo(self, objeto, graus):
        pontos = objeto.getPontos()
        tipo = objeto.getTipo()
        novosPontos = self.__Rotacao(pontos, graus)
        self.__renderizar(tipo, novosPontos)

    #errado
    def __RotacaoCentroObjeto(self, objeto, graus):
        pontos = objeto.getPontos()
        tipo = objeto.getTipo()
        deslocamento = []
        i = 0
        for i in pontos:
            deslocamento[i] = pontos[i] * (-1)
        novosPontos = self.__Transladar(pontos, deslocamento)
        novaPosicao = self.__Rotacao(novosPontos)


    def __RotacaoCentroArbitrario(self, objeto, graus, centro):
        pontos = objeto.getPontos()
        tipo = objeto.getTipo()

    def __Rotacao(self, pontos, graus):
        novosPontos = []
        i = 0
        for i in pontos:
            if(i % 2 == 0):
                novosPontos[i] = pontos[i] * math.cos(graus) - pontos[i + 1] * math.sin(graus)
            else:
                novosPontos[i] = pontos[i - 1] * math.sin(graus) - pontos[i] * math.cos(graus)
        return novosPontos

if __name__ == "__main__":
    root = QApplication(sys.argv)
    app = Janela()
    app.show()
    sys.exit(root.exec_())
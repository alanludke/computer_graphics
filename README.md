# Computer_graphics - INE5420-05208 (20212)

Sistema básico com window e viewport 

# Objetivo

O objetivo dos exercícios propostos na Parte I é a construção, passo a passo, de um Sistema Gráfico Interativo capaz de representar, em perspectiva realista, objetos em 3D como modelos de arame e também como superfícies bicúbicas renderizadas como malhas de curvas.

# NTH

- Display file para 2D capaz de representar pontos, segmentos de retas e polígonos (listas de pontos interconectados), onde: Cada objeto possui um nome, cada objeto possui um tipo e sua lista de  coordenadas de tamanho variável dependendo de seu tipo. Para facilitar a sua vida mais tarde, chame o objeto polígono de wireframe;
- Transformação de viewport em 2D;
- Funções de Panning/navegação 2D (movimentação do window);
- Funções de Zooming (modificação do tamanho do window);

# Requisitos

- Use a linguagem Python 3;
- Use uma biblioteca como Tkinker ou PyQt para implementar a GUI;
- Use apenas as diretivas de desenho de pontos e linhas para exibir os objetos no canvas, não use drawPolygon e afins;
- Caso a entrada das coordenadas não seja feita com cliques do mouse no canvas, o sistema deve aceitar entradas no seguinte padrão:
```
(x1, y1),(x2, y2),...
```
- Código para parsing:
```
pontos: List[Tuple[float]] = list(eval([input string]))
```
- A transformada de viewport não deve distorcer os objetos. Ex.: Se um objeto for um quadrado, ele deve ser exibido como tal.

# Como usar

Primeiramente você deve definir um ambiente virtual a partir do comando:

```
virtualenv venv
```

Ativa-lo com o seguinte comando:
```
source venv/bin/activate
```

E instalar as libs(com suas determinadas versões) em seu venv
```
pip install -r requirements.txt
```
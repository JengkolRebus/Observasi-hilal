import matplotlib.pyplot as plt
from PyQt5 import QtWidgets
from PyQt5.Qt import Qt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas

class MyView(QtWidgets.QGraphicsView):
    def __init__(self):
        QtWidgets.QGraphicsView.__init__(self)

        scene = QtWidgets.QGraphicsScene(self)
        self.scene = scene

        figure = Figure()
        axes = figure.gca()
        axes.set_title("title")
        axes.plot(plt.contourf(xx, yy, Z,cmap=plt.cm.autumn, alpha=0.8))
        canvas = FigureCanvas(figure)
        canvas.setGeometry(0, 0, 500, 500)
        scene.addWidget(canvas)

        self.setScene(scene)
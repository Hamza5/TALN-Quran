from PyQt4.QtGui import QWidget
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
from GUI.HistogramTab import Ui_HistogramForme
from Functions.Histgramme import histoplot
from Functions.QuranCorpus import parse_quranic_corpus

class Main(QWidget, Ui_HistogramForme):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.fig_dict = {}

    def addfig(self, name, fig):
        self.fig_dict[name] = fig
        self.mplfigs.addItem(name)

    def addmpl(self, fig):
        self.canvas = FigureCanvas(fig)
        self.figureGroupBox.layout().addWidget(self.canvas)
        self.canvas.draw()
        self.toolbar = NavigationToolbar(self.canvas,
                                         self.figureGroupBox, coordinates=True)
        self.figureGroupBox.layout().addWidget(self.toolbar)

if __name__ == '__main__':
    import sys
    from PyQt4 import QtGui
    import numpy as np

    fig1 = Figure()
    ax1f1 = fig1.add_subplot(111)
    ax1f1.plot(np.random.rand(5))

    quran = parse_quranic_corpus("../quranic-corpus-morphology-0.4.txt")

    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.addmpl(histoplot(2, 2, 5, quran))
    main.show()
    sys.exit(app.exec_())
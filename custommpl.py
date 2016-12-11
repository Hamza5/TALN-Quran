from PyQt4.QtGui import QWidget
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
from HistogramTab import Ui_Form


class Main(QWidget, Ui_Form):
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


from QuranCorpus import parse_quranic_corpus


def load(file):
    f = open(file, 'rU', encoding='utf-8')
    return f.read()


def index_ahkam(file_ahkam):
    file = load(file_ahkam)
    spliedfile = file.split(")")
    ahkam_dict = dict()
    ayate_dict = dict()
    prev_sourat = 1
    for aya in spliedfile:
        if aya == "\n" or aya == "":
            break
        splited_aya = aya.split("(")
        sourat_mad = splited_aya[0]
        aya_sourat = splited_aya[1].split(":")
        sourat_number = aya_sourat[0]
        aya_number = aya_sourat[1]
        ayate_dict[int(aya_number)] = sourat_mad
        if int(aya_number) == 1:
            ahkam_dict[prev_sourat] = ayate_dict.copy()
            prev_sourat = int(sourat_number)
            ayate_dict.clear()
        if int(sourat_number) == 114 and int(aya_number) == 6:
            ahkam_dict[int(sourat_number)] = ayate_dict.copy()
            ayate_dict.clear()
    return ahkam_dict


def histoplot(sourate, deb, fin, quran):
    elements = []
    labels = []
    index_ahkam1 = index_ahkam("ahkaam_encoding.txt")
    counts = {i: 0 for i in 'aiouA'}
    addedspace = 0;
    for ayat in range(deb, fin):
        label = list(index_ahkam1[sourate + 1][ayat])
        addedspace = 0
        ayastring = quran[sourate][ayat]
        for word in str(ayastring).split(" "):
            numerVoy = 0
            for char in str(word):
                if char in counts:
                    numerVoy += 1
            addedspace += numerVoy
            labels.append(word)
            labels.extend([''] * (numerVoy - 1))
        elements.extend(label)
        if len(label) - addedspace >= 0:
            labels.extend([''] * (len(label) - addedspace))
        else:
            elements.extend(['0'] * (addedspace - len(label)))
    resultat = list(map(int, elements))

    plt.figure()
    plt.gca().invert_yaxis()
    y_pos = np.arange(len(labels))
    performance = resultat
    plt.barh(y_pos, performance, align='center', alpha=1)
    plt.yticks(y_pos, labels, rotation='horizontal')
    plt.xlabel('مد')
    plt.title('Histogram')

    # figure = Figure()
    # figure.gca().invert_yaxis()
    # y_pos = np.arange(len(labels))
    # performance = resultat
    # # figure.barh(y_pos, performance, align='center', alpha=1)
    # figure.set_label(performance)
    # figure.yticks(y_pos, labels, rotation='horizontal')
    # figure.xlabel('مد')
    # figure.title('Histogram')

    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    # ax.barh(y_pos, performance, align='center', alpha=1)
    # ax.set_yticks(y_pos, labels, rotation='horizontal')
    #
    # ax.axvline(0, color='k', lw=3)  # poor man's zero level
    #
    # ax.set_xlabel('مد')
    # ax.set_title('Histogram')
    # ax.grid(True)
    return plt

if __name__ == '__main__':
    import sys
    from PyQt4 import QtGui
    import numpy as np

    fig1 = Figure()
    ax1f1 = fig1.add_subplot(111)
    ax1f1.plot(np.random.rand(5))
    # quran = parse_quranic_corpus("Quran/quranic-corpus-morphology-0.4.txt")
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.addmpl(fig1)
    main.show()
    sys.exit(app.exec_())
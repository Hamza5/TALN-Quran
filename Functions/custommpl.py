from PyQt4.QtGui import QWidget
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
from GUI.HistogramTab import Ui_HistogramForme
from Functions.Histgramme import histoplot
from Functions.QuranCorpus import parse_quranic_corpus
from Functions.Selector import Selector
from PyQt4.QtGui import QMessageBox
class Main(QWidget, Ui_HistogramForme):
    def __init__(self , quran ,AhkIndex):
        super(Main, self).__init__()
        self.setupUi(self)
        self.fig_dict = {}
        self.quran = quran
        self.ahkamIndex = AhkIndex
        self.addmpl(histoplot(0, 0, 0, quran, "Histogramme",self.ahkamIndex))
        self.pushButtonChoisirFin.setEnabled(False)
        self.ChoisirDebut.clicked.connect(self.choisirDebutFunc)
        self.pushButtonChoisirFin.clicked.connect(self.choisirFinFunc)
        self.pushButtonGenerer.clicked.connect(self.pushButtonGenererFunc)
        self.pushButtonPrecedent.clicked.connect(self.pushButtonPrecedentFunc)
        self.pushButtonSuivant.clicked.connect(self.pushButtonSuivantFunc)


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
    def choisirDebutFunc(self):
        self.s = Selector(self.quran)
        if self.s.exec_() == self.s.Accepted:
            self.pushButtonChoisirFin.setEnabled(True)
            self.souratDebut,self.ayaDebut, mot = self.s.selection()
            self.lineEditSouratDebut.setText(str(self.souratDebut))
            self.lineEdit_AyaDebut.setText(str(self.ayaDebut))
    def choisirFinFunc(self):
        self.sel = Selector(self.quran)
        self.sel.souratComboBox.setEnabled(False)
        self.sel.souratComboBox.setCurrentIndex(self.s.souratComboBox.currentIndex())
        if self.sel.exec_() == self.sel.Accepted:
            self.souratFin, self.ayaFin, mot = self.sel.selection()
            self.lineEdit_SouratFin.setText(str(self.souratFin))
            self.lineEdit_AyaFin.setText(str(self.ayaFin))
    def redrow(self, sourat, ayadeb, ayafin, title):
        self.canvas = FigureCanvas(histoplot(sourat, ayadeb, ayafin, self.quran, title,self.ahkamIndex))
        for i in reversed(range(self.figureGroupBox.layout().count())):
            self.figureGroupBox.layout().itemAt(i).widget().setParent(None)
        self.figureGroupBox.layout().addWidget(self.canvas)
        self.canvas.draw()
        self.toolbar = NavigationToolbar(self.canvas,
                                         self.figureGroupBox, coordinates=True)
        self.figureGroupBox.layout().addWidget(self.toolbar)
    def titles(self, sourat, aya1, aya2):
        return "Histogramme :"+str(sourat)+" ["+str(aya1)+", "+str(aya2)+"]"
    def pushButtonGenererFunc(self):
        if self.lineEditSouratDebut.text() == "" or self.lineEdit_SouratFin.text() == "" :
            QMessageBox.critical(self, "Erreur", "Il faut d'abord choisir un intervalle de Ayat")
        elif self.ayaDebut > self.ayaFin:
            QMessageBox.critical(self, "Erreur", "Il faut respecter l'ordre de Ayat")
        else:
            self.AyaCourant = self.ayaDebut
            if self.AyaCourant+3 < self.ayaFin:
                self.redrow(self.souratDebut, self.AyaCourant, self.AyaCourant + 3,self.titles(self.souratDebut,self.AyaCourant,self.AyaCourant + 3))
                self.AyaCourant = + 3
            else :
                self.pushButtonSuivant.setEnabled(False)
                self.pushButtonPrecedent.setEnabled(False)
                self.redrow(self.souratDebut, self.AyaCourant,  self.ayaFin+1, self.titles(self.souratDebut,self.AyaCourant,self.ayaFin+1))
                self.AyaCourant = self.ayaFin

    def pushButtonSuivantFunc(self):
        if self.AyaCourant + 3 < self.ayaFin:
            self.redrow(self.souratDebut, self.AyaCourant, self.AyaCourant + 3,self.titles(self.souratDebut,self.AyaCourant,self.AyaCourant+3))
            self.AyaCourant += 3
        else :
            self.pushButtonSuivant.setEnabled(False)
            self.redrow(self.souratDebut, self.AyaCourant, self.ayaFin, self.titles(self.souratDebut, self.AyaCourant, self.ayaFin))
            self.AyaCourant = self.ayaFin
    def pushButtonPrecedentFunc(self):
        if self.AyaCourant - 3 > 0:
            self.redrow(self.souratDebut, self.AyaCourant - 3, self.AyaCourant, self.titles(self.souratDebut,self.AyaCourant -3,self.AyaCourant))
            self.AyaCourant -= 3
            self.pushButtonSuivant.setEnabled(True)
        else:
            self.pushButtonPrecedent.setEnabled(False)
            self.redrow(self.souratDebut, 0, self.AyaCourant , self.titles(self.souratDebut,1,self.AyaCourant))
            self.AyaCourant = 0

if __name__ == '__main__':
    import sys
    from PyQt4 import QtGui
    import numpy as np
    from Functions.Histgramme import index_ahkam
    fig1 = Figure()
    ax1f1 = fig1.add_subplot(111)
    ax1f1.plot(np.random.rand(5))

    quran = parse_quranic_corpus("../quranic-corpus-morphology-0.4.txt")
    AhkIndex = index_ahkam("../ahkaam_encoding.txt")
    app = QtGui.QApplication(sys.argv)
    main = Main(quran ,AhkIndex)
    main.show()
    sys.exit(app.exec_())
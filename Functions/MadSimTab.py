from PyQt4.QtGui import QWidget
from PyQt4.QtGui import QFileDialog
from PyQt4.QtGui import QMessageBox
from GUI.Chercher_Mad import Ui_Recherche_Q
from Functions.MadSim import Madsim
import io
class Main(QWidget, Ui_Recherche_Q):
    def __init__(self,quran, ahkaam_encoding):
        super(Main, self).__init__()
        self.quran = quran
        self.ahkaam_encoding = ahkaam_encoding
        self.setupUi(self)
        self.RechercheQ_RehBTN.clicked.connect(self.buttonTrouveClicked)
        self.RechercheQEnreg.clicked.connect(self.buttonEnregClicked)
    def buttonTrouveClicked(self):
        if self.lineEdit_RechercheQ.text() == "":
            QMessageBox.critical(self, "Erreur", "Aucune série d'élongations a été saisie")
        elif not self.lineEdit_RechercheQ.text().isdigit():
            QMessageBox.critical(self, "Erreur", "La serie d'élongations est incorrect")
        else:
            list_ = Madsim(self.lineEdit_RechercheQ.text(), self.quran,self.ahkaam_encoding)
            self.RechercheQ_textEdit.append("Resultat trouvé pour la serie: "+self.lineEdit_RechercheQ.text())
            for elem in list_:
                self.RechercheQ_textEdit.append("{1!s:10} {0}".format(elem.arabic_text(), elem.location()))

    def buttonEnregClicked(self):
        path = QFileDialog.getSaveFileName(self, filter='Texte (*.txt)')
        text = self.RechercheQ_textEdit.toPlainText()
        with io.open(path, 'w', encoding='utf8') as f:
            f.write(text)
            f.close()


if __name__ == '__main__':
    import sys
    from PyQt4 import QtGui
    app = QtGui.QApplication(sys.argv)
    from Functions.QuranCorpus import parse_quranic_corpus
    quran = parse_quranic_corpus("../quranic-corpus-morphology-0.4.txt")
    main = Main(quran, "../ahkaam_encoding.txt")
    main.show()
    sys.exit(app.exec_())


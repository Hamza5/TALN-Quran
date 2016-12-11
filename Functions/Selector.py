from GUI.SelectorDialog import Ui_SelectorDialog
from PyQt4.QtGui import QDialog, QApplication
from Functions.QuranCorpus import Quran, parse_quranic_corpus


class Selector(QDialog, Ui_SelectorDialog):

    def __init__(self, quran, parent=None):
        if not isinstance(quran, Quran):
            raise TypeError('quran must be Quran')
        super(Selector, self).__init__(parent)
        self.setupUi(self)
        self.quran = quran
        for sourat in self.quran:
            self.souratComboBox.addItem(str(sourat))
        self.fill_ayats()
        self.fill_words()
        self.display_content()

        self.souratComboBox.currentIndexChanged.connect(self.fill_ayats)
        self.ayatComboBox.currentIndexChanged.connect(self.fill_words)

        self.souratComboBox.currentIndexChanged.connect(self.display_content)
        self.ayatComboBox.currentIndexChanged.connect(self.display_content)
        self.wordComboBox.currentIndexChanged.connect(self.display_content)

        self.ayatCheckBox.toggled.connect(self.display_content)
        self.wordCheckBox.toggled.connect(self.display_content)

        self.wordCheckBox.toggled.connect(self.wordComboBox.setEnabled)
        self.ayatCheckBox.toggled.connect(self.wordComboBox.setEnabled)
        self.ayatCheckBox.toggled.connect(self.ayatComboBox.setEnabled)
        self.ayatCheckBox.toggled.connect(self.wordCheckBox.setEnabled)
        self.ayatCheckBox.toggled.connect(self.wordCheckBox.setChecked)

    def fill_ayats(self):
        sourat_num = self.souratComboBox.currentIndex()+1
        self.ayatComboBox.clear()
        for ayat in self.quran[sourat_num]:
            self.ayatComboBox.addItem(str(int(ayat)))
        self.fill_words()

    def fill_words(self):
        sourat_num = self.souratComboBox.currentIndex()+1
        self.wordComboBox.clear()
        if self.ayatComboBox.currentText() != '':
            ayat_num = int(self.ayatComboBox.currentText())
            for word in self.quran[sourat_num][ayat_num]:
                self.wordComboBox.addItem(str(int(word)))

    def display_content(self):
        sourat_num = self.souratComboBox.currentIndex()+1
        if self.ayatComboBox.currentText() != '':
            ayat_num = int(self.ayatComboBox.currentText())
            if self.wordComboBox.currentText() != '':
                word_num = int(self.wordComboBox.currentText())
                if self.wordCheckBox.isChecked():
                    self.selectedTextEdit.setText(self.quran[sourat_num][ayat_num][word_num].arabic_text())
                elif self.ayatCheckBox.isChecked():
                    self.selectedTextEdit.setText(self.quran[sourat_num][ayat_num].arabic_text())
                else:
                    self.selectedTextEdit.clear()
                    first_ayats = self.quran[sourat_num][1:10]
                    for ayat in first_ayats:
                        self.selectedTextEdit.append(ayat.arabic_text()+' ('+str(ayat.location()[1])+') ')

    def selection(self):
        sourat_num = self.souratComboBox.currentIndex()+1
        ayat_num = int(self.ayatComboBox.currentText())
        word_num = int(self.wordComboBox.currentText())
        return sourat_num, ayat_num, word_num

if __name__ == '__main__':
    app = QApplication([])
    quran_full = parse_quranic_corpus('../quranic-corpus-morphology-0.4.txt')
    s = Selector(quran_full)
    s.show()
    app.exec()

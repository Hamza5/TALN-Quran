from PyQt4.QtGui import QWidget, QMessageBox, QFileDialog
from PyQt4.QtCore import QThread
from GUI.TransliterationTab import Ui_TransliterationTab
from Functions.QuranTransliteration import quran_buckwalter_scheme, transliterate_to_ascii, transliterate_to_arabic
from Functions.Selector import Selector


class ConvertThread(QThread):

    def __init__(self, parent=None):
        super(ConvertThread, self).__init__(parent)
        self.result = ''
        self.error = None

    def run(self):
        transliteration_tab = self.parent()
        assert isinstance(transliteration_tab, Transliteration)
        try:
            if transliteration_tab.transliterationSourceInputRadioButton.isChecked():
                text = transliteration_tab.transliterationTextSourcePlainTextEdit.toPlainText()
                if text[0] in quran_buckwalter_scheme.keys():  # User has entered buckwalter text
                    self.result = transliterate_to_arabic(text)
                else:
                    self.result = transliterate_to_ascii(text)
            else:
                with open(transliteration_tab.transliterationSourceFileLineEdit.text(), encoding='utf-8') as file:
                    line = file.readline().rstrip('\n')
                    if line[0] in quran_buckwalter_scheme.keys():  # User has entered buckwalter text
                        transliterate = transliterate_to_arabic
                    else:
                        transliterate = transliterate_to_ascii
                    self.result += transliterate(line) + '\n'
                    for line in file:
                        self.result += transliterate(line.rstrip('\n')) + '\n'
        except Exception as err:
            self.error = err


class Transliteration(QWidget, Ui_TransliterationTab):

    def __init__(self, quran, parent=None):
        super(Transliteration, self).__init__(parent)
        self.setupUi(self)

        self.quran = quran
        self.button_old_text = self.transliterationConvertPushButton.text()

        self.convert_thread = ConvertThread(self)
        self.convert_thread.started.connect(self.before_start)
        self.convert_thread.finished.connect(self.after_end)

        self.transliterationConvertPushButton.clicked.connect(self.convert)
        self.transliterationResultFilePushButton.clicked.connect(self.save)
        self.transliterationSourceFilePushButton.clicked.connect(self.select_file)
        self.transliterationSourceTextSelectPushButton.clicked.connect(self.select_quran_part)

        self.transliterationTextSourcePlainTextEdit.textChanged.connect(self.enable_convert)
        self.transliterationSourceFileLineEdit.textChanged.connect(self.enable_convert)
        self.transliterationSourceInputRadioButton.toggled.connect(self.enable_convert)

    def convert(self):
        self.convert_thread.start()

    def before_start(self):
        self.transliterationConvertPushButton.setText('Conversion en cours...')
        self.transliterationConvertPushButton.setEnabled(False)

    def after_end(self):
        self.transliterationConvertPushButton.setText(self.button_old_text)
        self.transliterationConvertPushButton.setEnabled(True)
        if not self.convert_thread.error:
            self.transliterationTextResultPlainTextEdit.setPlainText(self.convert_thread.result)
        else:
            err = self.convert_thread.error
            if isinstance(err, OSError):
                QMessageBox.critical(self, 'Projet TALN - Erreur',
                                     'Impossible de lire le fichier {} !'.format(err.filename))
            elif isinstance(err,(UnicodeError, IndexError)):
                QMessageBox.critical(self, 'Projet TALN - Erreur',
                                     'Le fichier n\'est pas un fichier texte valide !')
            else:
                QMessageBox.critical(self, 'Projet TALN - Erreur',
                                     'Vous avez saisi des caractères invalides !\nLes caractères autorisés sont les caractères coraniques arabes ou buckwalter.')

    def save(self):
        path = QFileDialog.getSaveFileName(self, filter='Texte (*.txt)')
        if path:
            try:
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(self.transliterationTextResultPlainTextEdit.toPlainText())
            except OSError as err:
                QMessageBox.critical(self, 'Projet TALN - Erreur', 'Impossible d\'écrir le fichier {} !'.format(err.filename))

    def select_file(self):
        path = QFileDialog.getOpenFileName(self, filter='Texte (*.txt)')
        if path:
            self.transliterationSourceFileLineEdit.setText(path)

    def enable_convert(self):
        cond = False
        if self.transliterationSourceInputRadioButton.isChecked() and self.transliterationTextSourcePlainTextEdit.toPlainText():
            cond = True
        elif self.transliterationSourceFileRadioButton.isChecked() and self.transliterationSourceFileLineEdit.text():
            cond = True
        self.transliterationConvertPushButton.setEnabled(cond)

    def select_quran_part(self):
        selection_dialog = Selector(self.quran, parent=self)
        if selection_dialog.exec() == selection_dialog.Accepted:
            sourat, ayat, word = selection_dialog.selection()
            if selection_dialog.ayat_selected() and selection_dialog.word_selected():
                self.transliterationTextSourcePlainTextEdit.setPlainText(self.quran[sourat][ayat][word].arabic_text())
            elif selection_dialog.ayat_selected():
                self.transliterationTextSourcePlainTextEdit.setPlainText(self.quran[sourat][ayat].arabic_text())
            else:
                for ayat in self.quran[sourat]:
                    self.transliterationTextSourcePlainTextEdit.appendPlainText(ayat.arabic_text())

if __name__ == '__main__':
    from PyQt4.QtGui import QApplication
    from Functions.QuranCorpus import parse_quranic_corpus
    app = QApplication([])
    s = Transliteration(parse_quranic_corpus('../quranic-corpus-morphology-0.4-last-14-sourats.txt'))
    s.show()
    app.exec()

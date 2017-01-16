from PyQt4.QtGui import QWidget, QMessageBox, QFileDialog, QColorDialog, QPalette, QColor
from PyQt4.QtCore import QThread
from GUI.ConcordanceTab import Ui_ConcordanceTab
from Functions.Selector import Selector
from Functions.QuranCorpus import concordance
from Functions.QuranTransliteration import transliterate_to_ascii, quran_buckwalter_scheme


class SearchThread(QThread):

    def run(self):
        concordance_tab = self.parent()
        assert isinstance(concordance_tab, Concordancer)
        word = concordance_tab.concordanceSourceLineEdit.text().strip()
        if word[0] in quran_buckwalter_scheme.values():
            word = transliterate_to_ascii(word)
        strict = concordance_tab.concordanceStrictSearchCheckBox.isChecked()
        basic = concordance_tab.concordanceSourceBasicSearchTypeCheckBox.isChecked()
        lemme = concordance_tab.concordanceSourceLemmeSearchTypeCheckBox.isChecked()
        root = concordance_tab.concordanceSourceRootSearchTypeCheckBox.isChecked()
        words_before = concordance_tab.concordanceSourceWordsBeforeSpinBox.value()
        words_after = concordance_tab.concordanceSourceWordsAfterSpinBox.value()
        self.results = concordance(word, concordance_tab.quran, words_before, words_after, strict, basic, lemme, root)


class Concordancer(QWidget, Ui_ConcordanceTab):

    def __init__(self, quran, parent=None):
        super(Concordancer, self).__init__(parent)
        self.setupUi(self)
        self.quran = quran
        self.search_thread = SearchThread(self)
        self.search_button_old_text = self.concordanceSearchPushButton.text()
        self.highlight_text_color = self.palette().color(QPalette.HighlightedText)
        self.highlight_background_color = self.palette().color(QPalette.Highlight)

        self.concordanceSourceSelectPushButton.clicked.connect(self.select_quran_word)
        self.concordanceSourceLineEdit.textChanged.connect(lambda: self.concordanceSearchPushButton.setEnabled(bool(self.concordanceSourceLineEdit.text())))
        self.concordanceResultsSavePushButton.clicked.connect(self.save)
        self.concordanceSourceFontColorPushButton.clicked.connect(self.select_font_color)
        self.concordanceSourceBackgroundColorPushButton.clicked.connect(self.select_highlight_color)

        self.concordanceSearchPushButton.clicked.connect(self.search)
        self.search_thread.started.connect(self.before_start)
        self.search_thread.finished.connect(self.after_end)

    def select_quran_word(self):
        selection_dialog = Selector(self.quran, parent=self)
        selection_dialog.wordCheckBox.setEnabled(False)
        selection_dialog.ayatCheckBox.setEnabled(False)
        if selection_dialog.exec() == selection_dialog.Accepted:
            sourat, ayat, word = selection_dialog.selection()
            self.concordanceSourceLineEdit.setText(self.quran[sourat][ayat][word].arabic_text())

    def search(self):
        word = self.concordanceSourceLineEdit.text().strip()
        if len(word.split()) > 1:
            QMessageBox.critical(self, 'Projet TALN - Erreur', 'Vous ne pouvez saisir qu\'un seul mot !')
        else:
            buckwalter = True
            arabic = True
            for char in word:  # Checking if the word is in Buckwalter encoding
                if char not in quran_buckwalter_scheme.keys():
                    buckwalter = False
                    break
            for char in word:  # Checking if the word is in Arabic encoding
                if char not in quran_buckwalter_scheme.values():
                    arabic = False
                    break
            if not arabic and not buckwalter:
                QMessageBox.critical(self, 'Projet TALN - Erreur', 'Vous ne pouvez utiliser que les lettres Coraniques ou Buckwalter !')
            else:
                self.search_thread.start()

    def before_start(self):
        self.concordanceSearchPushButton.setEnabled(False)
        self.concordanceSearchPushButton.setText('Recherche en cours...')

    def after_end(self):
        displayed_content = '''
                        <!DOCTYPE HTML>
                        <html>
                            <head>
                                <meta charset="UTF-8">
                                <style type="text/css">
                                    body {
                                        direction : rtl;
                                    }
                                    em {
                                        background-color : %s;
                                        color : %s;
                                    }
                                    p {
                                        font-style : italic;
                                    }
                                </style>
                            </head>
                            <body>
                    ''' % (self.highlight_background_color.name(), self.highlight_text_color.name())
        contexts, indexes, scores = self.search_thread.results
        if len(contexts):
            displayed_content += '<ol>'
            for context, index, score in zip(contexts, indexes, scores):
                displayed_content += '<li>{} '.format(context[index].location()[:-1])
                last_ayat = context[0].location()[1]
                for i in range(len(context)):
                    current_ayat = context[i].location()[1]
                    if last_ayat != current_ayat:
                        displayed_content += '[{}] '.format(last_ayat)
                        last_ayat = current_ayat
                    if i == index:
                        displayed_content += '<em>{}</em> '.format(context[i].arabic_text())
                    else:
                        displayed_content += '{} '.format(context[i].arabic_text())
                displayed_content += '</li>'
            displayed_content += '</ol>'
        else:
            displayed_content += '<p>Aucun résultat trouvé !</p>'
        displayed_content += '''
                            </body>
                        </html>
                    '''
        self.concordanceResultsTextEdit.setHtml(displayed_content)
        self.concordanceSearchPushButton.setText(self.search_button_old_text)
        self.concordanceSearchPushButton.setEnabled(True)

    def save(self):
        path = QFileDialog.getSaveFileName(self, filter='HTML (*.html)')
        if path:
            try:
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(self.concordanceResultsTextEdit.toHtml())
            except OSError as err:
                QMessageBox.critical(self, 'Projet TALN - Erreur',
                                     'Impossible d\'écrir le fichier {} !'.format(err.filename))

    def select_font_color(self):
        color = QColorDialog.getColor(self.highlight_text_color, self, "Sélectionner une couleur")
        assert isinstance(color, QColor)
        if color.isValid():
            self.highlight_text_color = color
            self.concordanceSourceFontColorPushButton.setStyleSheet('QWidget { color : %s; background-color : %s;}' % (color.name(), color.lighter().name()))

    def select_highlight_color(self):
        color = QColorDialog.getColor(self.highlight_background_color, self, "Sélectionner une couleur")
        assert isinstance(color, QColor)
        if color.isValid():
            self.highlight_background_color = color
            self.concordanceSourceBackgroundColorPushButton.setStyleSheet('QWidget { background-color : %s; color : %s;}' % (color.name(), color.darker().name()))


if __name__ == '__main__':
    from PyQt4.QtGui import QApplication
    from Functions.QuranCorpus import parse_quranic_corpus
    app = QApplication([])
    quran_ = parse_quranic_corpus('../quranic-corpus-morphology-0.4-last-14-sourats.txt')
    c = Concordancer(quran_)
    c.show()
    app.exec()

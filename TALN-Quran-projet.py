import sys
from os.path import join, dirname
from PyQt4.QtGui import QApplication, QMainWindow, QTabWidget, QDialog, QMessageBox, QFileDialog, QVBoxLayout
from PyQt4.QtCore import QLocale, QThread, pyqtSignal
from GUI.SplashDialog import Ui_SplashDialog
from Functions.Transliteration import Transliteration
from Functions.Concordancer import Concordancer
from Functions.QuranCorpus import Quran, parse_quranic_corpus
from Functions.MadSim import index_ahkam
from Functions.MadSimTab import Main as MadSim
from Functions.custommpl import Main as Histogram


class QuranicCorpusThread(QThread):

    progress_changed = pyqtSignal(int)

    def __init__(self, parent=None):
        super(QuranicCorpusThread, self).__init__(parent)
        self.quran = None
        self.error = None

    def run(self):
        splash_window = self.parent()
        assert isinstance(splash_window, Splash)
        try:
            self.quran = parse_quranic_corpus(splash_window.quranicCorpusPathLineEdit.text(), self.update_progress)
        except Exception as err:
            self.error = err

    def update_progress(self, current):
        self.progress_changed.emit(current)


class AhkaamEncodingThread(QThread):

    progress_changed = pyqtSignal(int)

    def __init__(self, parent=None):
        super(AhkaamEncodingThread, self).__init__(parent)
        self.ahkaam = None
        self.error = None

    def run(self):
        splash_window = self.parent()
        assert isinstance(splash_window, Splash)
        try:
            self.ahkaam = index_ahkam(splash_window.ahkaamEncodingPathLineEdit.text(), self.update_progress)
        except Exception as err:
            self.error = err

    def update_progress(self, progress):
        self.progress_changed.emit(progress)


class Splash(QDialog, Ui_SplashDialog):

    def __init__(self, application, parent=None):
        super(Splash, self).__init__(parent)
        QLocale.setDefault(QLocale(QLocale.French))
        self.setupUi(self)

        self.app = application
        self.window = None

        self.quranic_corpus_thread = QuranicCorpusThread(self)
        self.quranic_corpus_thread.started.connect(self.before_start_quranic_corpus)
        self.quranic_corpus_thread.finished.connect(self.after_end_quranic_corpus)
        self.quranic_corpus_thread.progress_changed.connect(self.loadingProgressBar.setValue)

        self.ahkaam_encoding_thread = AhkaamEncodingThread(self)
        self.ahkaam_encoding_thread.started.connect(self.before_ahkaam_encoding)
        self.ahkaam_encoding_thread.finished.connect(self.after_ahkaam_encoding)
        self.ahkaam_encoding_thread.progress_changed.connect(self.loadingProgressBar.setValue)

        self.loadingProgressBar.setVisible(False)
        self.quranicCorpusPathLineEdit.setText(join(dirname(__file__), 'quranic-corpus-morphology-0.4.txt'))
        self.ahkaamEncodingPathLineEdit.setText(join(dirname(__file__), 'ahkaam_encoding.txt'))

        self.quranicCorpusSelectPushButton.clicked.connect(self.select_quranic_corpus)
        self.ahkaamEncodingSelectPushButton.clicked.connect(self.select_ahkaam_encoding)
        self.launchPushButton.clicked.connect(self.launch)

    def before_start_quranic_corpus(self):
        self.launchPushButton.setVisible(False)
        self.loadingProgressBar.setVisible(True)
        self.loadingProgressBar.setFormat('Chargement du corpus Coranique %p%')

    def after_end_quranic_corpus(self):
        if self.quranic_corpus_thread.error:
            self.launchPushButton.setVisible(True)
            self.loadingProgressBar.setVisible(False)
            err = self.quranic_corpus_thread.error
            if isinstance(err, OSError):
                QMessageBox.critical(self, 'Projet TALN - Erreur',
                                     'Impossible de lire le fichier {} !'.format(err.filename))
            else:
                QMessageBox.critical(self, 'Projet TALN - Erreur',
                                     'Le fichier du corpus est invalide !')
        else:
            self.ahkaam_encoding_thread.start()

    def before_ahkaam_encoding(self):
        self.loadingProgressBar.setValue(0)
        self.loadingProgressBar.setFormat('Chargement du Ahkaam encoding %p%')

    def after_ahkaam_encoding(self):
        if self.ahkaam_encoding_thread.error:
            self.launchPushButton.setVisible(True)
            self.loadingProgressBar.setVisible(False)
            err = self.ahkaam_encoding_thread.error
            if isinstance(err, OSError):
                QMessageBox.critical(self, 'Projet TALN - Erreur',
                                     'Impossible de lire le fichier {} !'.format(err.filename))
            else:
                QMessageBox.critical(self, 'Projet TALN - Erreur',
                                     'Erreur lors de la lecture du fichier d\'ahkaam !')
        else:
            self.window = MainWindow(self.quranic_corpus_thread.quran, self.ahkaam_encoding_thread.ahkaam)
            self.window.move(self.app.desktop().availableGeometry().center() - self.window.rect().center())
            self.window.show()
            self.hide()

    def launch(self):
        self.quranic_corpus_thread.start()

    def select_quranic_corpus(self):
        path = QFileDialog.getOpenFileName(self, filter='Texte (*.txt)')
        if path:
            self.quranicCorpusPathLineEdit.setText(path)

    def select_ahkaam_encoding(self):
        path = QFileDialog.getOpenFileName(self, filter='Texte (*.txt)')
        if path:
            self.ahkaamEncodingPathLineEdit.setText(path)


class MainWindow(QMainWindow):

    def __init__(self, quran, ahkaam):
        if not isinstance(quran, Quran):
            raise TypeError('quran must be Quran')
        super(MainWindow, self).__init__()
        QLocale.setDefault(QLocale(QLocale.French))
        self.tabs = QTabWidget(self)
        transliteration_tab = Transliteration(quran, self)
        concordance_tab = Concordancer(quran, self)
        madsim_tab = MadSim(quran, ahkaam)
        histogram_tab = Histogram(quran, ahkaam)
        self.tabs.addTab(transliteration_tab, transliteration_tab.windowTitle())
        self.tabs.addTab(concordance_tab, concordance_tab.windowTitle())
        self.tabs.addTab(madsim_tab, madsim_tab.windowTitle())
        self.tabs.addTab(histogram_tab, histogram_tab.windowTitle())
        self.setCentralWidget(self.tabs)
        self.setWindowTitle('Projet TALN - ABBAD & ZEBOUCHI')


app = QApplication(sys.argv)
splash = Splash(app)
splash.move(app.desktop().availableGeometry().center() - splash.rect().center())  # Center the window on the screen
splash.show()
sys.exit(app.exec())

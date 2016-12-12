# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/SplashDialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_SplashDialog(object):
    def setupUi(self, SplashDialog):
        SplashDialog.setObjectName(_fromUtf8("SplashDialog"))
        SplashDialog.resize(472, 291)
        self.verticalLayout = QtGui.QVBoxLayout(SplashDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.quranicCorpusGroupBox = QtGui.QGroupBox(SplashDialog)
        self.quranicCorpusGroupBox.setObjectName(_fromUtf8("quranicCorpusGroupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.quranicCorpusGroupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.quranicCorpusPathLineEdit = QtGui.QLineEdit(self.quranicCorpusGroupBox)
        self.quranicCorpusPathLineEdit.setObjectName(_fromUtf8("quranicCorpusPathLineEdit"))
        self.horizontalLayout.addWidget(self.quranicCorpusPathLineEdit)
        self.quranicCorpusSelectPushButton = QtGui.QPushButton(self.quranicCorpusGroupBox)
        self.quranicCorpusSelectPushButton.setObjectName(_fromUtf8("quranicCorpusSelectPushButton"))
        self.horizontalLayout.addWidget(self.quranicCorpusSelectPushButton)
        self.verticalLayout.addWidget(self.quranicCorpusGroupBox)
        self.ahkaamEncodingGroupBox = QtGui.QGroupBox(SplashDialog)
        self.ahkaamEncodingGroupBox.setObjectName(_fromUtf8("ahkaamEncodingGroupBox"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.ahkaamEncodingGroupBox)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.ahkaamEncodingPathLineEdit = QtGui.QLineEdit(self.ahkaamEncodingGroupBox)
        self.ahkaamEncodingPathLineEdit.setObjectName(_fromUtf8("ahkaamEncodingPathLineEdit"))
        self.horizontalLayout_2.addWidget(self.ahkaamEncodingPathLineEdit)
        self.ahkaamEncodingSelectPushButton = QtGui.QPushButton(self.ahkaamEncodingGroupBox)
        self.ahkaamEncodingSelectPushButton.setObjectName(_fromUtf8("ahkaamEncodingSelectPushButton"))
        self.horizontalLayout_2.addWidget(self.ahkaamEncodingSelectPushButton)
        self.verticalLayout.addWidget(self.ahkaamEncodingGroupBox)
        self.launchPushButton = QtGui.QPushButton(SplashDialog)
        self.launchPushButton.setObjectName(_fromUtf8("launchPushButton"))
        self.verticalLayout.addWidget(self.launchPushButton)
        self.loadingProgressBar = QtGui.QProgressBar(SplashDialog)
        self.loadingProgressBar.setLocale(QtCore.QLocale(QtCore.QLocale.French, QtCore.QLocale.France))
        self.loadingProgressBar.setProperty("value", 0)
        self.loadingProgressBar.setObjectName(_fromUtf8("loadingProgressBar"))
        self.verticalLayout.addWidget(self.loadingProgressBar)

        self.retranslateUi(SplashDialog)
        QtCore.QMetaObject.connectSlotsByName(SplashDialog)

    def retranslateUi(self, SplashDialog):
        SplashDialog.setWindowTitle(_translate("SplashDialog", "Projet TALN - Démarrage", None))
        self.quranicCorpusGroupBox.setTitle(_translate("SplashDialog", "Emplacement du corpus coranique", None))
        self.quranicCorpusSelectPushButton.setText(_translate("SplashDialog", "Sélectionner", None))
        self.ahkaamEncodingGroupBox.setTitle(_translate("SplashDialog", "Emplacement du fichier d\'encodage d\'ahkaam", None))
        self.ahkaamEncodingSelectPushButton.setText(_translate("SplashDialog", "Sélectionner", None))
        self.launchPushButton.setText(_translate("SplashDialog", "Démarrer", None))


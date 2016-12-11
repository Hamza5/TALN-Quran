# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/TransliterationTab.ui'
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

class Ui_TransliterationTab(object):
    def setupUi(self, TransliterationTab):
        TransliterationTab.setObjectName(_fromUtf8("TransliterationTab"))
        TransliterationTab.resize(778, 591)
        TransliterationTab.setLocale(QtCore.QLocale(QtCore.QLocale.French, QtCore.QLocale.France))
        self.verticalLayout = QtGui.QVBoxLayout(TransliterationTab)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.transliterationSourceGroupBox = QtGui.QGroupBox(TransliterationTab)
        self.transliterationSourceGroupBox.setObjectName(_fromUtf8("transliterationSourceGroupBox"))
        self.gridLayout = QtGui.QGridLayout(self.transliterationSourceGroupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.transliterationSourceFileLineEdit = QtGui.QLineEdit(self.transliterationSourceGroupBox)
        self.transliterationSourceFileLineEdit.setEnabled(False)
        self.transliterationSourceFileLineEdit.setObjectName(_fromUtf8("transliterationSourceFileLineEdit"))
        self.gridLayout.addWidget(self.transliterationSourceFileLineEdit, 2, 1, 1, 1)
        self.transliterationSourceInputRadioButton = QtGui.QRadioButton(self.transliterationSourceGroupBox)
        self.transliterationSourceInputRadioButton.setChecked(True)
        self.transliterationSourceInputRadioButton.setObjectName(_fromUtf8("transliterationSourceInputRadioButton"))
        self.gridLayout.addWidget(self.transliterationSourceInputRadioButton, 1, 0, 1, 1)
        self.transliterationSourceFileRadioButton = QtGui.QRadioButton(self.transliterationSourceGroupBox)
        self.transliterationSourceFileRadioButton.setObjectName(_fromUtf8("transliterationSourceFileRadioButton"))
        self.gridLayout.addWidget(self.transliterationSourceFileRadioButton, 2, 0, 1, 1)
        self.transliterationSourceFilePushButton = QtGui.QPushButton(self.transliterationSourceGroupBox)
        self.transliterationSourceFilePushButton.setEnabled(False)
        self.transliterationSourceFilePushButton.setObjectName(_fromUtf8("transliterationSourceFilePushButton"))
        self.gridLayout.addWidget(self.transliterationSourceFilePushButton, 2, 2, 1, 1)
        self.transliterationTextSourcePlainTextEdit = QtGui.QPlainTextEdit(self.transliterationSourceGroupBox)
        self.transliterationTextSourcePlainTextEdit.setObjectName(_fromUtf8("transliterationTextSourcePlainTextEdit"))
        self.gridLayout.addWidget(self.transliterationTextSourcePlainTextEdit, 1, 1, 1, 1)
        self.transliterationSourceTextSelectPushButton = QtGui.QPushButton(self.transliterationSourceGroupBox)
        self.transliterationSourceTextSelectPushButton.setObjectName(_fromUtf8("transliterationSourceTextSelectPushButton"))
        self.gridLayout.addWidget(self.transliterationSourceTextSelectPushButton, 1, 2, 1, 1)
        self.verticalLayout.addWidget(self.transliterationSourceGroupBox)
        self.transliterationConvertPushButton = QtGui.QPushButton(TransliterationTab)
        self.transliterationConvertPushButton.setEnabled(False)
        self.transliterationConvertPushButton.setObjectName(_fromUtf8("transliterationConvertPushButton"))
        self.verticalLayout.addWidget(self.transliterationConvertPushButton)
        self.transliterationResultGroupBox = QtGui.QGroupBox(TransliterationTab)
        self.transliterationResultGroupBox.setObjectName(_fromUtf8("transliterationResultGroupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.transliterationResultGroupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.transliterationTextResultPlainTextEdit = QtGui.QPlainTextEdit(self.transliterationResultGroupBox)
        self.transliterationTextResultPlainTextEdit.setReadOnly(True)
        self.transliterationTextResultPlainTextEdit.setObjectName(_fromUtf8("transliterationTextResultPlainTextEdit"))
        self.verticalLayout_2.addWidget(self.transliterationTextResultPlainTextEdit)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.transliterationResultFilePushButton = QtGui.QPushButton(self.transliterationResultGroupBox)
        self.transliterationResultFilePushButton.setEnabled(True)
        self.transliterationResultFilePushButton.setObjectName(_fromUtf8("transliterationResultFilePushButton"))
        self.horizontalLayout_2.addWidget(self.transliterationResultFilePushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.transliterationResultGroupBox)

        self.retranslateUi(TransliterationTab)
        QtCore.QObject.connect(self.transliterationSourceInputRadioButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.transliterationTextSourcePlainTextEdit.setEnabled)
        QtCore.QObject.connect(self.transliterationSourceFileRadioButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.transliterationSourceFileLineEdit.setEnabled)
        QtCore.QObject.connect(self.transliterationSourceFileRadioButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.transliterationSourceFilePushButton.setEnabled)
        QtCore.QObject.connect(self.transliterationSourceInputRadioButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.transliterationSourceTextSelectPushButton.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(TransliterationTab)

    def retranslateUi(self, TransliterationTab):
        TransliterationTab.setWindowTitle(_translate("TransliterationTab", "Translitération", None))
        self.transliterationSourceGroupBox.setTitle(_translate("TransliterationTab", "Source", None))
        self.transliterationSourceInputRadioButton.setText(_translate("TransliterationTab", "Texte", None))
        self.transliterationSourceFileRadioButton.setText(_translate("TransliterationTab", "Fichier", None))
        self.transliterationSourceFilePushButton.setText(_translate("TransliterationTab", "Parcourir", None))
        self.transliterationSourceTextSelectPushButton.setText(_translate("TransliterationTab", "Sélectionner", None))
        self.transliterationConvertPushButton.setText(_translate("TransliterationTab", "Convertir", None))
        self.transliterationResultGroupBox.setTitle(_translate("TransliterationTab", "Résultat", None))
        self.transliterationResultFilePushButton.setText(_translate("TransliterationTab", "Enregistrer", None))


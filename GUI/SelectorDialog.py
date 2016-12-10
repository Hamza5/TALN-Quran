# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/SelectorDialog.ui'
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

class Ui_SelectorDialog(object):
    def setupUi(self, SelectorDialog):
        SelectorDialog.setObjectName(_fromUtf8("SelectorDialog"))
        SelectorDialog.resize(519, 410)
        SelectorDialog.setLocale(QtCore.QLocale(QtCore.QLocale.French, QtCore.QLocale.France))
        self.verticalLayout = QtGui.QVBoxLayout(SelectorDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.selectGroupBox = QtGui.QGroupBox(SelectorDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectGroupBox.sizePolicy().hasHeightForWidth())
        self.selectGroupBox.setSizePolicy(sizePolicy)
        self.selectGroupBox.setObjectName(_fromUtf8("selectGroupBox"))
        self.gridLayout = QtGui.QGridLayout(self.selectGroupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.souratLabel = QtGui.QLabel(self.selectGroupBox)
        self.souratLabel.setObjectName(_fromUtf8("souratLabel"))
        self.gridLayout.addWidget(self.souratLabel, 0, 0, 1, 1)
        self.souratComboBox = QtGui.QComboBox(self.selectGroupBox)
        self.souratComboBox.setObjectName(_fromUtf8("souratComboBox"))
        self.gridLayout.addWidget(self.souratComboBox, 1, 0, 1, 1)
        self.ayatComboBox = QtGui.QComboBox(self.selectGroupBox)
        self.ayatComboBox.setObjectName(_fromUtf8("ayatComboBox"))
        self.gridLayout.addWidget(self.ayatComboBox, 1, 1, 1, 1)
        self.wordComboBox = QtGui.QComboBox(self.selectGroupBox)
        self.wordComboBox.setObjectName(_fromUtf8("wordComboBox"))
        self.gridLayout.addWidget(self.wordComboBox, 1, 2, 1, 1)
        self.ayatCheckBox = QtGui.QCheckBox(self.selectGroupBox)
        self.ayatCheckBox.setChecked(True)
        self.ayatCheckBox.setObjectName(_fromUtf8("ayatCheckBox"))
        self.gridLayout.addWidget(self.ayatCheckBox, 0, 1, 1, 1)
        self.wordCheckBox = QtGui.QCheckBox(self.selectGroupBox)
        self.wordCheckBox.setChecked(True)
        self.wordCheckBox.setObjectName(_fromUtf8("wordCheckBox"))
        self.gridLayout.addWidget(self.wordCheckBox, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.selectGroupBox)
        self.selectedTextEdit = QtGui.QTextEdit(SelectorDialog)
        self.selectedTextEdit.setReadOnly(True)
        self.selectedTextEdit.setObjectName(_fromUtf8("selectedTextEdit"))
        self.verticalLayout.addWidget(self.selectedTextEdit)
        self.buttonsBox = QtGui.QDialogButtonBox(SelectorDialog)
        self.buttonsBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonsBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonsBox.setObjectName(_fromUtf8("buttonsBox"))
        self.verticalLayout.addWidget(self.buttonsBox)

        self.retranslateUi(SelectorDialog)
        QtCore.QObject.connect(self.buttonsBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SelectorDialog.accept)
        QtCore.QObject.connect(self.buttonsBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SelectorDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SelectorDialog)

    def retranslateUi(self, SelectorDialog):
        SelectorDialog.setWindowTitle(_translate("SelectorDialog", "Projet TALN - Sélectionner", None))
        self.selectGroupBox.setTitle(_translate("SelectorDialog", "Sélectionner une partie du Quran", None))
        self.souratLabel.setText(_translate("SelectorDialog", "Sourate", None))
        self.ayatCheckBox.setText(_translate("SelectorDialog", "Verset", None))
        self.wordCheckBox.setText(_translate("SelectorDialog", "Mot", None))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Chercher_Mad.ui'
#
# Created: Sun Dec 11 12:54:49 2016
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_Recherche_Q(object):
    def setupUi(self, Recherche_Q):
        Recherche_Q.setObjectName(_fromUtf8("Recherche_Q"))
        Recherche_Q.resize(730, 456)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Recherche_Q)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEdit_RechercheQ = QtGui.QLineEdit(Recherche_Q)
        self.lineEdit_RechercheQ.setObjectName(_fromUtf8("lineEdit_RechercheQ"))
        self.horizontalLayout.addWidget(self.lineEdit_RechercheQ)
        self.RechercheQ_RehBTN = QtGui.QPushButton(Recherche_Q)
        self.RechercheQ_RehBTN.setObjectName(_fromUtf8("RechercheQ_RehBTN"))
        self.horizontalLayout.addWidget(self.RechercheQ_RehBTN)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.CherhcherMad_GRpBox = QtGui.QGroupBox(Recherche_Q)
        self.CherhcherMad_GRpBox.setObjectName(_fromUtf8("CherhcherMad_GRpBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.CherhcherMad_GRpBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.RechercheQ_textEdit = QtGui.QTextEdit(self.CherhcherMad_GRpBox)
        self.RechercheQ_textEdit.setReadOnly(True)
        self.RechercheQ_textEdit.setObjectName(_fromUtf8("RechercheQ_textEdit"))
        self.verticalLayout.addWidget(self.RechercheQ_textEdit)
        self.verticalLayout_2.addWidget(self.CherhcherMad_GRpBox)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.RechercheQEnreg = QtGui.QPushButton(Recherche_Q)
        self.RechercheQEnreg.setObjectName(_fromUtf8("RechercheQEnreg"))
        self.horizontalLayout_2.addWidget(self.RechercheQEnreg)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Recherche_Q)
        QtCore.QMetaObject.connectSlotsByName(Recherche_Q)

    def retranslateUi(self, Recherche_Q):
        Recherche_Q.setWindowTitle(_translate("Recherche_Q", "Form", None))
        self.lineEdit_RechercheQ.setPlaceholderText(_translate("Recherche_Q", "Veuillez entrer une serie de Moudoud a chercher", None))
        self.RechercheQ_RehBTN.setText(_translate("Recherche_Q", "Trouver", None))
        self.CherhcherMad_GRpBox.setTitle(_translate("Recherche_Q", "Resultat trouvé", None))
        self.RechercheQEnreg.setText(_translate("Recherche_Q", "Enregistrer", None))


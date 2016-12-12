# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/ConcordanceTab.ui'
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

class Ui_ConcordanceTab(object):
    def setupUi(self, ConcordanceTab):
        ConcordanceTab.setObjectName(_fromUtf8("ConcordanceTab"))
        ConcordanceTab.resize(826, 562)
        ConcordanceTab.setLocale(QtCore.QLocale(QtCore.QLocale.French, QtCore.QLocale.France))
        self.verticalLayout_2 = QtGui.QVBoxLayout(ConcordanceTab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.concordanceSourceGroupBox = QtGui.QGroupBox(ConcordanceTab)
        self.concordanceSourceGroupBox.setObjectName(_fromUtf8("concordanceSourceGroupBox"))
        self.gridLayout = QtGui.QGridLayout(self.concordanceSourceGroupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.concordanceSourceWordsBeforeLabel = QtGui.QLabel(self.concordanceSourceGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.concordanceSourceWordsBeforeLabel.sizePolicy().hasHeightForWidth())
        self.concordanceSourceWordsBeforeLabel.setSizePolicy(sizePolicy)
        self.concordanceSourceWordsBeforeLabel.setObjectName(_fromUtf8("concordanceSourceWordsBeforeLabel"))
        self.gridLayout.addWidget(self.concordanceSourceWordsBeforeLabel, 2, 0, 1, 1)
        self.concordanceSourceWordsAfterSpinBox = QtGui.QSpinBox(self.concordanceSourceGroupBox)
        self.concordanceSourceWordsAfterSpinBox.setMinimum(0)
        self.concordanceSourceWordsAfterSpinBox.setMaximum(20)
        self.concordanceSourceWordsAfterSpinBox.setProperty("value", 3)
        self.concordanceSourceWordsAfterSpinBox.setObjectName(_fromUtf8("concordanceSourceWordsAfterSpinBox"))
        self.gridLayout.addWidget(self.concordanceSourceWordsAfterSpinBox, 2, 3, 1, 1)
        self.concordanceSourceWordsAfterLabel = QtGui.QLabel(self.concordanceSourceGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.concordanceSourceWordsAfterLabel.sizePolicy().hasHeightForWidth())
        self.concordanceSourceWordsAfterLabel.setSizePolicy(sizePolicy)
        self.concordanceSourceWordsAfterLabel.setObjectName(_fromUtf8("concordanceSourceWordsAfterLabel"))
        self.gridLayout.addWidget(self.concordanceSourceWordsAfterLabel, 2, 2, 1, 1)
        self.concordanceSourceWordsBeforeSpinBox = QtGui.QSpinBox(self.concordanceSourceGroupBox)
        self.concordanceSourceWordsBeforeSpinBox.setMinimum(0)
        self.concordanceSourceWordsBeforeSpinBox.setMaximum(20)
        self.concordanceSourceWordsBeforeSpinBox.setProperty("value", 3)
        self.concordanceSourceWordsBeforeSpinBox.setObjectName(_fromUtf8("concordanceSourceWordsBeforeSpinBox"))
        self.gridLayout.addWidget(self.concordanceSourceWordsBeforeSpinBox, 2, 1, 1, 1)
        self.concordanceStrictSearchCheckBox = QtGui.QCheckBox(self.concordanceSourceGroupBox)
        self.concordanceStrictSearchCheckBox.setObjectName(_fromUtf8("concordanceStrictSearchCheckBox"))
        self.gridLayout.addWidget(self.concordanceStrictSearchCheckBox, 2, 4, 1, 1)
        self.concordanceSourceSelectPushButton = QtGui.QPushButton(self.concordanceSourceGroupBox)
        self.concordanceSourceSelectPushButton.setAutoDefault(False)
        self.concordanceSourceSelectPushButton.setObjectName(_fromUtf8("concordanceSourceSelectPushButton"))
        self.gridLayout.addWidget(self.concordanceSourceSelectPushButton, 0, 4, 1, 1)
        self.concordanceSourceLineEdit = QtGui.QLineEdit(self.concordanceSourceGroupBox)
        self.concordanceSourceLineEdit.setObjectName(_fromUtf8("concordanceSourceLineEdit"))
        self.gridLayout.addWidget(self.concordanceSourceLineEdit, 0, 0, 1, 4)
        self.verticalLayout_2.addWidget(self.concordanceSourceGroupBox)
        self.concordanceSearchPushButton = QtGui.QPushButton(ConcordanceTab)
        self.concordanceSearchPushButton.setEnabled(False)
        self.concordanceSearchPushButton.setDefault(True)
        self.concordanceSearchPushButton.setObjectName(_fromUtf8("concordanceSearchPushButton"))
        self.verticalLayout_2.addWidget(self.concordanceSearchPushButton)
        self.concordanceResultsGroupBox = QtGui.QGroupBox(ConcordanceTab)
        self.concordanceResultsGroupBox.setObjectName(_fromUtf8("concordanceResultsGroupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.concordanceResultsGroupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.concordanceResultsTextEdit = QtGui.QTextEdit(self.concordanceResultsGroupBox)
        self.concordanceResultsTextEdit.setReadOnly(True)
        self.concordanceResultsTextEdit.setObjectName(_fromUtf8("concordanceResultsTextEdit"))
        self.verticalLayout.addWidget(self.concordanceResultsTextEdit)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.concordanceResultsSavePushButton = QtGui.QPushButton(self.concordanceResultsGroupBox)
        self.concordanceResultsSavePushButton.setObjectName(_fromUtf8("concordanceResultsSavePushButton"))
        self.horizontalLayout.addWidget(self.concordanceResultsSavePushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.concordanceResultsGroupBox)

        self.retranslateUi(ConcordanceTab)
        QtCore.QMetaObject.connectSlotsByName(ConcordanceTab)

    def retranslateUi(self, ConcordanceTab):
        ConcordanceTab.setWindowTitle(_translate("ConcordanceTab", "Concordanceur", None))
        self.concordanceSourceGroupBox.setTitle(_translate("ConcordanceTab", "Recherche d\'un mot", None))
        self.concordanceSourceWordsBeforeLabel.setText(_translate("ConcordanceTab", "Nombre de mots avant", None))
        self.concordanceSourceWordsAfterLabel.setText(_translate("ConcordanceTab", "Nombre de mots après", None))
        self.concordanceStrictSearchCheckBox.setText(_translate("ConcordanceTab", "Recherche stricte", None))
        self.concordanceSourceSelectPushButton.setText(_translate("ConcordanceTab", "Sélectionner", None))
        self.concordanceSourceLineEdit.setPlaceholderText(_translate("ConcordanceTab", "Votre mot", None))
        self.concordanceSearchPushButton.setText(_translate("ConcordanceTab", "Rechercher", None))
        self.concordanceResultsGroupBox.setTitle(_translate("ConcordanceTab", "Résultats", None))
        self.concordanceResultsSavePushButton.setText(_translate("ConcordanceTab", "Enregistrer", None))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HistogramTab.ui'
#
# Created: Sun Dec 11 12:27:49 2016
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

class Ui_HistogramForme(object):
    def setupUi(self, HistogramForme):
        HistogramForme.setObjectName(_fromUtf8("HistogramForme"))
        HistogramForme.resize(599, 386)
        self.mplvl = QtGui.QVBoxLayout(HistogramForme)
        self.mplvl.setObjectName(_fromUtf8("mplvl"))
        self.comboBox = QtGui.QComboBox(HistogramForme)
        self.comboBox.setMinimumSize(QtCore.QSize(581, 0))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.mplvl.addWidget(self.comboBox, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.figureGroupBox = QtGui.QGroupBox(HistogramForme)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.figureGroupBox.sizePolicy().hasHeightForWidth())
        self.figureGroupBox.setSizePolicy(sizePolicy)
        self.figureGroupBox.setObjectName(_fromUtf8("figureGroupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.figureGroupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.mplvl.addWidget(self.figureGroupBox)
        self.widget = QtGui.QWidget(HistogramForme)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pushButtonSuivant = QtGui.QPushButton(self.widget)
        self.pushButtonSuivant.setFlat(False)
        self.pushButtonSuivant.setObjectName(_fromUtf8("pushButtonSuivant"))
        self.gridLayout_2.addWidget(self.pushButtonSuivant, 0, 1, 1, 1)
        self.pushButtonPrecedent = QtGui.QPushButton(self.widget)
        self.pushButtonPrecedent.setObjectName(_fromUtf8("pushButtonPrecedent"))
        self.gridLayout_2.addWidget(self.pushButtonPrecedent, 0, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.mplvl.addWidget(self.widget)

        self.retranslateUi(HistogramForme)
        QtCore.QMetaObject.connectSlotsByName(HistogramForme)

    def retranslateUi(self, HistogramForme):
        HistogramForme.setWindowTitle(_translate("HistogramForme", "Form", None))
        self.figureGroupBox.setTitle(_translate("HistogramForme", "Histogramme", None))
        self.pushButtonSuivant.setText(_translate("HistogramForme", "Suivant", None))
        self.pushButtonPrecedent.setText(_translate("HistogramForme", "Precedent", None))


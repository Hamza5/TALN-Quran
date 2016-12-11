# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HistogramTab.ui'
#
# Created: Sun Dec 11 09:37:40 2016
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(599, 386)
        self.mplvl = QtGui.QVBoxLayout(Form)
        self.mplvl.setObjectName(_fromUtf8("mplvl"))
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setMinimumSize(QtCore.QSize(581, 0))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.mplvl.addWidget(self.comboBox, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.figureGroupBox = QtGui.QGroupBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.figureGroupBox.sizePolicy().hasHeightForWidth())
        self.figureGroupBox.setSizePolicy(sizePolicy)
        self.figureGroupBox.setObjectName(_fromUtf8("figureGroupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.figureGroupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.mplvl.addWidget(self.figureGroupBox)
        self.widget = QtGui.QWidget(Form)
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
        self.pushButton_2 = QtGui.QPushButton(self.widget)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout_2.addWidget(self.pushButton_2, 0, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(self.widget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_2.addWidget(self.pushButton, 0, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.mplvl.addWidget(self.widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.figureGroupBox.setTitle(_translate("Form", "Histogramme", None))
        self.pushButton_2.setText(_translate("Form", "Suivant", None))
        self.pushButton.setText(_translate("Form", "Precedent", None))


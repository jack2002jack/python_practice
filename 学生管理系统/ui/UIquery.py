# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIquery.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_queryPanel(object):
    def setupUi(self, queryPanel):
        queryPanel.setObjectName("queryPanel")
        queryPanel.resize(231, 101)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(queryPanel)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox = QtWidgets.QComboBox(queryPanel)
        self.comboBox.setMaximumSize(QtCore.QSize(60, 16777215))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.lineEdit = QtWidgets.QLineEdit(queryPanel)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(queryPanel)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(queryPanel)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)

        self.retranslateUi(queryPanel)
        QtCore.QMetaObject.connectSlotsByName(queryPanel)

    def retranslateUi(self, queryPanel):
        _translate = QtCore.QCoreApplication.translate
        queryPanel.setWindowTitle(_translate("queryPanel", "Form"))
        self.comboBox.setItemText(0, _translate("queryPanel", "学号"))
        self.comboBox.setItemText(1, _translate("queryPanel", "姓名"))
        self.comboBox.setItemText(2, _translate("queryPanel", "班级"))
        self.comboBox.setItemText(3, _translate("queryPanel", "性别"))
        self.comboBox.setItemText(4, _translate("queryPanel", "年龄"))
        self.comboBox.setItemText(5, _translate("queryPanel", "电话"))
        self.comboBox.setItemText(6, _translate("queryPanel", "QQ"))
        self.comboBox.setItemText(7, _translate("queryPanel", "地址"))
        self.pushButton.setText(_translate("queryPanel", "开始查询"))
        self.pushButton_2.setText(_translate("queryPanel", "重置"))

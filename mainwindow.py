# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FinddleHelper(object):
    def setupUi(self, FinddleHelper):
        FinddleHelper.setObjectName("FinddleHelper")
        FinddleHelper.resize(617, 287)
        FinddleHelper.setMinimumSize(QtCore.QSize(617, 287))
        FinddleHelper.setMaximumSize(QtCore.QSize(617, 287))
        self.centralwidget = QtWidgets.QWidget(FinddleHelper)
        self.centralwidget.setMinimumSize(QtCore.QSize(617, 265))
        self.centralwidget.setMaximumSize(QtCore.QSize(617, 265))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 611, 261))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setSizeIncrement(QtCore.QSize(0, 0))
        self.lineEdit.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(22)
        font.setItalic(False)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.button_start = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_start.sizePolicy().hasHeightForWidth())
        self.button_start.setSizePolicy(sizePolicy)
        self.button_start.setMaximumSize(QtCore.QSize(120, 20))
        self.button_start.setObjectName("button_start")
        self.verticalLayout_2.addWidget(self.button_start)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.button_reset = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_reset.sizePolicy().hasHeightForWidth())
        self.button_reset.setSizePolicy(sizePolicy)
        self.button_reset.setMaximumSize(QtCore.QSize(50, 20))
        self.button_reset.setObjectName("button_reset")
        self.horizontalLayout_2.addWidget(self.button_reset)
        self.button_copy = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_copy.sizePolicy().hasHeightForWidth())
        self.button_copy.setSizePolicy(sizePolicy)
        self.button_copy.setMaximumSize(QtCore.QSize(50, 20))
        self.button_copy.setObjectName("button_copy")
        self.horizontalLayout_2.addWidget(self.button_copy)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideRight)
        self.tableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.tableWidget)
        FinddleHelper.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(FinddleHelper)
        self.statusbar.setObjectName("statusbar")
        FinddleHelper.setStatusBar(self.statusbar)

        self.retranslateUi(FinddleHelper)
        QtCore.QMetaObject.connectSlotsByName(FinddleHelper)

    def retranslateUi(self, FinddleHelper):
        _translate = QtCore.QCoreApplication.translate
        FinddleHelper.setWindowTitle(_translate("FinddleHelper", "FinddleHelper"))
        self.button_start.setText(_translate("FinddleHelper", "开始"))
        self.button_reset.setText(_translate("FinddleHelper", "重置"))
        self.button_copy.setText(_translate("FinddleHelper", "复制"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("FinddleHelper", "网址"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("FinddleHelper", "方式"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("FinddleHelper", "状态"))
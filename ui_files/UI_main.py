# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(887, 428)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.originLabel = QtWidgets.QLabel(self.centralwidget)
        self.originLabel.setText("")
        self.originLabel.setObjectName("originLabel")
        self.verticalLayout.addWidget(self.originLabel)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_2.addWidget(self.checkBox)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.removeButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeButton.setObjectName("removeButton")
        self.horizontalLayout_2.addWidget(self.removeButton)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(1, 4)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.removeBGLabel = QtWidgets.QLabel(self.centralwidget)
        self.removeBGLabel.setText("")
        self.removeBGLabel.setObjectName("removeBGLabel")
        self.verticalLayout_2.addWidget(self.removeBGLabel)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.previewPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.previewPushButton.setObjectName("previewPushButton")
        self.horizontalLayout_3.addWidget(self.previewPushButton)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem11)
        self.saveResultpushButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveResultpushButton.setObjectName("saveResultpushButton")
        self.horizontalLayout_3.addWidget(self.saveResultpushButton)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem12)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.setStretch(1, 4)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.blueRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.blueRadioButton.setChecked(True)
        self.blueRadioButton.setObjectName("blueRadioButton")
        self.colorButtonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.colorButtonGroup.setObjectName("colorButtonGroup")
        self.colorButtonGroup.addButton(self.blueRadioButton)
        self.verticalLayout_4.addWidget(self.blueRadioButton)
        self.redRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.redRadioButton.setObjectName("redRadioButton")
        self.colorButtonGroup.addButton(self.redRadioButton)
        self.verticalLayout_4.addWidget(self.redRadioButton)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        spacerItem13 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem13)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        
        self.sizeButtonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.sizeButtonGroup.setObjectName("sizeButtonGroup")
        self.oneRadioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.oneRadioButton_4.setChecked(True)
        self.oneRadioButton_4.setObjectName("oneRadioButton_4")
        self.sizeButtonGroup.addButton(self.oneRadioButton_4)
        self.verticalLayout_3.addWidget(self.oneRadioButton_4)
        self.oneRadioButton_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.oneRadioButton_5.setObjectName("oneRadioButton_5")
        self.sizeButtonGroup.addButton(self.oneRadioButton_5)
        self.verticalLayout_3.addWidget(self.oneRadioButton_5)
        self.oneRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.oneRadioButton.setObjectName("oneRadioButton")
        self.sizeButtonGroup.addButton(self.oneRadioButton)
        self.verticalLayout_3.addWidget(self.oneRadioButton)
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setObjectName("radioButton_4")
        self.sizeButtonGroup.addButton(self.radioButton_4)
        self.verticalLayout_3.addWidget(self.radioButton_4)
        self.oneRadioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.oneRadioButton_2.setObjectName("oneRadioButton_2")
        self.sizeButtonGroup.addButton(self.oneRadioButton_2)
        self.verticalLayout_3.addWidget(self.oneRadioButton_2)
        self.radioButton_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_5.setObjectName("radioButton_5")
        self.sizeButtonGroup.addButton(self.radioButton_5)
        self.verticalLayout_3.addWidget(self.radioButton_5)
        self.oneRadioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.oneRadioButton_3.setObjectName("oneRadioButton_3")
        self.sizeButtonGroup.addButton(self.oneRadioButton_3)
        self.verticalLayout_3.addWidget(self.oneRadioButton_3)
       
        self.radioButton_6 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_6.setObjectName("radioButton_6")
        self.sizeButtonGroup.addButton(self.radioButton_6)
        self.verticalLayout_3.addWidget(self.radioButton_6)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.IndesignLabel = QtWidgets.QLabel(self.centralwidget)
        self.IndesignLabel.setMinimumSize(QtCore.QSize(400, 0))
        self.IndesignLabel.setText("")
        self.IndesignLabel.setObjectName("IndesignLabel")
        self.verticalLayout_6.addWidget(self.IndesignLabel)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem14)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_5.addWidget(self.pushButton_5)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem15)
        self.openPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.openPushButton.setEnabled(False)
        self.openPushButton.setObjectName("openPushButton")
        self.horizontalLayout_5.addWidget(self.openPushButton)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem16)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.verticalLayout_6.setStretch(0, 5)
        self.horizontalLayout_6.addLayout(self.verticalLayout_6)
        self.horizontalLayout_6.setStretch(3, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 887, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.helpAction = QtWidgets.QAction(MainWindow)
        self.helpAction.setObjectName("helpAction")
        self.declareAction = QtWidgets.QAction(MainWindow)
        self.declareAction.setObjectName("declareAction")
        self.aboutAction = QtWidgets.QAction(MainWindow)
        self.aboutAction.setObjectName("aboutAction")
        self.menu.addAction(self.helpAction)
        self.menu.addAction(self.declareAction)
        self.menu.addAction(self.aboutAction)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.colorButtonGroup.buttonClicked['int'].connect(MainWindow.colorSelectAction)
        self.pushButton.clicked.connect(MainWindow.selectPhotoAction)
        self.removeButton.clicked.connect(MainWindow.removeBackgroundAction)
        self.previewPushButton.clicked.connect(MainWindow.amplifyAction)
        self.saveResultpushButton.clicked.connect(MainWindow.saveRemoveResultAction)
        self.pushButton_5.clicked.connect(MainWindow.saveDesignResultAction)
        self.sizeButtonGroup.buttonClicked['int'].connect(MainWindow.sizeSelectAction)
        self.helpAction.triggered.connect(MainWindow.helpAction)
        self.aboutAction.triggered.connect(MainWindow.aboutAction)
        self.declareAction.triggered.connect(MainWindow.declareAction)
        self.openPushButton.clicked.connect(MainWindow.openSaveAction)
        self.checkBox.clicked['bool'].connect(MainWindow.noRemoveAction)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "照片抠图及证件照制作"))
        self.label.setText(_translate("MainWindow", "原图"))
        self.checkBox.setText(_translate("MainWindow", "不抠图"))
        self.pushButton.setText(_translate("MainWindow", "选择"))
        self.removeButton.setText(_translate("MainWindow", "抠图"))
        self.label_4.setText(_translate("MainWindow", "抠图后"))
        self.previewPushButton.setText(_translate("MainWindow", "查看抠图"))
        self.saveResultpushButton.setText(_translate("MainWindow", "保存抠图"))
        self.label_6.setText(_translate("MainWindow", "底色"))
        self.blueRadioButton.setText(_translate("MainWindow", "蓝色"))
        self.redRadioButton.setText(_translate("MainWindow", "红色"))
        self.label_7.setText(_translate("MainWindow", "尺寸"))
        self.oneRadioButton_4.setText(_translate("MainWindow", "一寸"))
        self.oneRadioButton_5.setText(_translate("MainWindow", "二寸"))
        self.oneRadioButton.setText(_translate("MainWindow", "一寸 x 五寸"))
        self.radioButton_4.setText(_translate("MainWindow", "二寸 x 五寸"))
        self.oneRadioButton_2.setText(_translate("MainWindow", "一寸 x 六寸"))
        self.radioButton_5.setText(_translate("MainWindow", "二寸 x 六寸"))
        self.oneRadioButton_3.setText(_translate("MainWindow", "5 寸混排"))
        self.radioButton_6.setText(_translate("MainWindow", "6 寸混排"))
        self.pushButton_5.setText(_translate("MainWindow", "保存排版"))
        self.openPushButton.setText(_translate("MainWindow", "打开保存"))
        self.menu.setTitle(_translate("MainWindow", "说明"))
        self.helpAction.setText(_translate("MainWindow", "操作说明"))
        self.declareAction.setText(_translate("MainWindow", "声明"))
        self.aboutAction.setText(_translate("MainWindow", "关于"))
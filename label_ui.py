# Form implementation generated from reading ui file 'label_ui.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(667, 414)
        Form.setWindowFlags(QtCore.Qt.WindowType.WindowStaysOnTopHint)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelQr = QtWidgets.QLabel(Form)
        self.labelQr.setObjectName("labelQr")
        self.verticalLayout.addWidget(self.labelQr)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.lineEditCaptureLabel = QtWidgets.QLineEdit(Form)
        self.lineEditCaptureLabel.setEnabled(False)
        self.lineEditCaptureLabel.setObjectName("lineEditCaptureLabel")
        self.horizontalLayout_3.addWidget(self.lineEditCaptureLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout.setStretch(0, 8)
        self.verticalLayout.setStretch(1, 2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 300))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.lineEditFirstLine = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEditFirstLine.setPlaceholderText("")
        self.lineEditFirstLine.setObjectName("lineEditFirstLine")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEditFirstLine)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.lineEditSecondLine = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEditSecondLine.setObjectName("lineEditSecondLine")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEditSecondLine)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_7)
        self.lineEditStep = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEditStep.setObjectName("lineEditStep")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEditStep)
        self.gridLayout_3.addLayout(self.formLayout_4, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.pushButtonStart = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButtonStart.setAutoDefault(False)
        self.pushButtonStart.setDefault(False)
        self.pushButtonStart.setObjectName("pushButtonStart")
        self.horizontalLayout_4.addWidget(self.pushButtonStart)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.lineEditCurrentLabel = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEditCurrentLabel.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEditCurrentLabel.setFont(font)
        self.lineEditCurrentLabel.setText("")
        self.lineEditCurrentLabel.setObjectName("lineEditCurrentLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEditCurrentLabel)
        self.verticalLayout_5.addLayout(self.formLayout_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButtonLast = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButtonLast.setEnabled(False)
        self.pushButtonLast.setObjectName("pushButtonLast")
        self.horizontalLayout_2.addWidget(self.pushButtonLast)
        self.pushButtonNext = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButtonNext.setEnabled(False)
        self.pushButtonNext.setObjectName("pushButtonNext")
        self.horizontalLayout_2.addWidget(self.pushButtonNext)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_6.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.verticalLayout_6)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 1, 1, 1)
        self.gridLayout.setColumnMinimumWidth(0, 6)
        self.gridLayout.setColumnMinimumWidth(1, 4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.labelQr.setText(_translate("Form", "Show QR Code Zone"))
        self.label_5.setText(_translate("Form", "Capture Label:"))
        self.groupBox_2.setTitle(_translate("Form", "Code Information"))
        self.label_4.setText(_translate("Form", "First Line:"))
        self.lineEditFirstLine.setText(_translate("Form", "CN-0J2RH2-C1501-"))
        self.label.setText(_translate("Form", "Second Line:"))
        self.lineEditSecondLine.setText(_translate("Form", "19F-057Y-A02"))
        self.label_7.setText(_translate("Form", "Step："))
        self.lineEditStep.setText(_translate("Form", "1"))
        self.lineEditStep.setPlaceholderText(_translate("Form", "hello"))
        self.pushButtonStart.setText(_translate("Form", "Start"))
        self.groupBox_3.setTitle(_translate("Form", "UN3481"))
        self.label_2.setText(_translate("Form", "Current Label："))
        self.pushButtonLast.setText(_translate("Form", "Last"))
        self.pushButtonNext.setText(_translate("Form", "Next"))

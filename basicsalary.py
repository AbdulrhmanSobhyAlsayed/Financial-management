# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'basicsalary.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import option
import Main
import login

class basicsalary(QtWidgets.QWidget):
    def __init__(self):
         super().__init__()
         self.initUI()
    def finish1(self):
         self.ui=option.option()
         self.close()
         self.ui.show()
    def close1(self):
         self.ui1=Main.main()
         self.close()
         self.ui1.show()
    def add(self):
         file1=open("exname.txt","r")
         name=file1.readline()
         file=open(str("%sbasicsalary.txt"%name),"a")
         file.write(str("%s\n%s\n"%(self.lineEdit.text(),self.lineEdit_2.text())))
         self.lineEdit.clear()
         self.lineEdit_2.clear()
    def initUI(self):
         self.setWindowTitle("Basic Salary")
         self.resize(425, 229)
         self.label = QtWidgets.QLabel(self)
         self.label.setGeometry(QtCore.QRect(40, 20, 341, 16))
         font = QtGui.QFont()
         font.setFamily("Times New Roman")
         font.setPointSize(10)
         font.setBold(True)
         font.setWeight(75)
         self.label.setFont(font)
         self.label.setObjectName("label")
         self.label_2 = QtWidgets.QLabel(self)
         self.label_2.setGeometry(QtCore.QRect(40, 40, 351, 16))
         font = QtGui.QFont()
         font.setFamily("Times New Roman")
         font.setPointSize(10)
         font.setBold(True)
         font.setWeight(75)
         self.label_2.setFont(font)
         self.label_2.setObjectName("label_2")
         self.label_3 = QtWidgets.QLabel(self)
         self.label_3.setGeometry(QtCore.QRect(40, 60, 311, 16))
         font = QtGui.QFont()
         font.setFamily("Times New Roman")
         font.setPointSize(10)
         font.setBold(True)
         font.setWeight(75)
         self.label_3.setFont(font)
         self.label_3.setObjectName("label_3")
         self.label_4 = QtWidgets.QLabel(self)
         self.label_4.setGeometry(QtCore.QRect(40, 100, 231, 16))
         font = QtGui.QFont()
         font.setFamily("Times New Roman")
         font.setPointSize(10)
         font.setBold(True)
         font.setWeight(75)
         self.label_4.setFont(font)
         self.label_4.setObjectName("label_4")
         self.lineEdit = QtWidgets.QLineEdit(self)
         self.lineEdit.setGeometry(QtCore.QRect(270, 100, 121, 20))
         self.lineEdit.setObjectName("lineEdit")
         self.label_5 = QtWidgets.QLabel(self)
         self.label_5.setGeometry(QtCore.QRect(40, 130, 241, 16))
         font = QtGui.QFont()
         font.setFamily("Times New Roman")
         font.setPointSize(10)
         font.setBold(True)
         font.setWeight(75)
         self.label_5.setFont(font)
         self.label_5.setObjectName("label_5")
         self.lineEdit_2 = QtWidgets.QLineEdit(self)
         self.lineEdit_2.setGeometry(QtCore.QRect(270, 130, 121, 20))
         self.lineEdit_2.setObjectName("lineEdit_2")
         self.pushButton = QtWidgets.QPushButton(self)
         self.pushButton.setGeometry(QtCore.QRect(40, 170, 91, 41))
         font = QtGui.QFont()
         font.setFamily("Times New Roman")
         font.setPointSize(10)
         font.setBold(True)
         font.setWeight(75)
         self.pushButton.setFont(font)
         self.pushButton.setObjectName("pushButton")
         self.pushButton.clicked.connect(self.add)
         self.pushButton_2 = QtWidgets.QPushButton(self)
         self.pushButton_2.setGeometry(QtCore.QRect(170, 170, 91, 41))
         font = QtGui.QFont()
         font.setFamily("Times New Roman")
         font.setPointSize(10)
         font.setBold(True)
         font.setWeight(75)
         self.pushButton_2.setFont(font)
         self.pushButton_2.setObjectName("pushButton_2")
         self.pushButton_2.clicked.connect(self.finish1)
         self.pushButton_3 = QtWidgets.QPushButton(self)
         self.pushButton_3.setGeometry(QtCore.QRect(290, 170, 91, 41))
         font = QtGui.QFont()
         font.setFamily("Times New Roman")
         font.setPointSize(10)
         font.setBold(True)
         font.setWeight(75)
         self.pushButton_3.setFont(font)
         self.pushButton_3.setObjectName("pushButton_3")
         self.pushButton_3.clicked.connect(self.close1)
         _translate = QtCore.QCoreApplication.translate
         self.label.setText(_translate("Dialog", "- If you want to add more basic salary sources enter Add."))
         self.label_2.setText(_translate("Dialog", "- If you have finished entering basic salary sources enter Finish."))
         self.label_3.setText(_translate("Dialog", "- If you want to exit enter close."))
         self.label_4.setText(_translate("Dialog", "Enter The Type Of  Basic Salary Source :"))
         self.label_5.setText(_translate("Dialog", "Enter The Value Of Salary    :"))
         self.pushButton.setText(_translate("Dialog", "Add"))
         self.pushButton_2.setText(_translate("Dialog", "Finish"))
         self.pushButton_3.setText(_translate("Dialog", "Close"))
         self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = basicsalary()
    sys.exit(app.exec_())


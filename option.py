# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'choose.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import Main
import expenses
import extraincome
import basicsalary
import debtforyou
import debtonyou
import balance

class option(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def mainwindow(self):
        self.close()
        self.ui=Main.main()
        self.ui.show()
    def exit(self):
        self.close()
    def expenses(self):
        self.close()
        self.ui1=expenses.expenses()
        self.ui1.show()
    def extraincome(self):
        self.close()
        self.ui2=extraincome.extraincome()
        self.ui2.show()
    def basicsalary(self):
        self.close()
        self.ui3=basicsalary.basicsalary()
        self.ui3.show()
    def debtforyou(self):
        self.close()
        self.ui4=debtforyou.debtforyou()
        self.ui4.show()
    def debtonyou(self):
        self.close()
        self.ui5=debtonyou.debtonyou()
        self.ui5.show()
    def balance(self):
        self.close()
        self.ui6=balance.balance()

    def initUI(self):
        self.setWindowTitle("Options")
        self.resize(240, 649)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(30, 10, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.basicsalary)
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 90, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.expenses)
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 170, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.extraincome)
        self.pushButton_4 = QtWidgets.QPushButton(self)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 250, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.debtforyou)
        self.pushButton_5 = QtWidgets.QPushButton(self)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 330, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.debtonyou)
        self.pushButton_6 = QtWidgets.QPushButton(self)
        self.pushButton_6.setGeometry(QtCore.QRect(30, 410, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.balance)
        self.pushButton_7 = QtWidgets.QPushButton(self)
        self.pushButton_7.setGeometry(QtCore.QRect(30, 490, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.mainwindow)
        self.pushButton_9 = QtWidgets.QPushButton(self)
        self.pushButton_9.setGeometry(QtCore.QRect(30, 570, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(self.exit)
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("Dialog", "Add Basic Salary"))
        self.pushButton_2.setText(_translate("Dialog", "Add Expenses"))
        self.pushButton_3.setText(_translate("Dialog", "Add Extra Income"))
        self.pushButton_4.setText(_translate("Dialog", "Add Debt For You"))
        self.pushButton_5.setText(_translate("Dialog", "Add Debt On You"))
        self.pushButton_6.setText(_translate("Dialog", "Get Balance "))
        self.pushButton_7.setText(_translate("Dialog", "Main Window"))
        self.pushButton_9.setText(_translate("Dialog", "Exit"))
        self.show()

      
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = option()
    sys.exit(app.exec_())


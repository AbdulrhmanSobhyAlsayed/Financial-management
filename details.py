# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'balance.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import option
import os
import re

class details(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.basicsalary=dict({})
        self.expenses=dict({})
        self.extraincome=dict({})
        self.debtforyou=dict({})
        self.debtonyou=dict({})
        self.initUI()
    def ok(self):
        self.ui=option.option()
        self.close()
    def dic(self,dic=dict({}),path=""):
        file= open("exname.txt","r")
        name=file.readline()
        file1=open(str("%s%s.txt"%(name,path)),"r")
        while (not(file1.tell() == os.fstat(file1.fileno()).st_size)):
            state=""
            key=file1.readline()
            value=file1.readline()
            key.replace(' ','')
            for key1 in dic.keys():
                if(re.sub("\s*", "", key1) == re.sub("\s*", "",key)):
                     state="r"
                     dic[key1]=str("%f\n"%(float(dic[key1])+float(value)))
            if(not(state=="r")):        
                 dic.update({key:value})
        print(dic)
        return dic
    def Name(self):
         file= open("exname.txt","r")
         name=file.readline()
         file1=open(str("%s.txt"%name),"r")
         name1=file1.readline()
         password=file1.readline()
         return str("*Your Name Is : %s\n*Your Password Is: %s"%(name1,password))
    def conv(self,d=dict({})):
         s=float(0)
         for key in d.values(): 
             s=s+float(key)
         return s 
    def detail(self):
        self.basicsalary=self.dic(self.basicsalary,"basicsalary")
        self.expenses=self.dic(self.expenses,"expenses")
        self.extraincome=self.dic(self.extraincome,"extraincome")
        self.debtforyou=self.dic(self.debtforyou,"debtforyou")
        self.debtonyou=self.dic(self.debtonyou,"debtonyou")
        basicsalary=self.conv(self.basicsalary)
        expenses=self.conv(self.expenses)
        extraincome=self.conv(self.extraincome)
        debtforyou=self.conv(self.debtforyou)
        debtonyou=self.conv(self.debtonyou)
        self.plainTextEdit.appendPlainText(self.Name())
        self.prints(self.basicsalary,"*Your Basic Salary Is :\n ")
        self.prints(self.extraincome,"*Your Extra Income Is :\n")
        self.prints(self.expenses,"*Your Expenses Is :\n")
        self.prints(self.debtforyou,"*Your Debit That You Will Have :\n")
        self.prints(self.debtonyou,"*Your Debit That You Will Pay :\n")
        self.plainTextEdit.appendPlainText(str("*Your Balance Is :\n%f\n"%(basicsalary+extraincome+debtforyou- expenses-debtonyou)))


    def prints(self,d=dict({}),tx=""):
        self.plainTextEdit.appendPlainText(tx) 
        for key,value in d.items():
           self.plainTextEdit.appendPlainText(str("%s%s"%(key,value)))
    def initUI(self):
        
        self.setWindowTitle("Balance")
        self.resize(400, 408)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self)
        self.plainTextEdit.setGeometry(QtCore.QRect(13, 10, 371, 331))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(145, 350, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.ok)
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("Dialog", "Ok"))
        self.detail()
        #self.plainTextEdit.setFont(font)
        #self.plainTextEdit.setDisabled(True)
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = details()
    sys.exit(app.exec_())


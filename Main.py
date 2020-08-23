from PyQt5 import QtCore, QtGui, QtWidgets
import login
import signup
import sys
class main(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def login(self):
        self.ui=login.login()
        self.close()
        self.ui.show()
    def signup(self):
        self.ui1=signup.signup()
        self.close()
        self.ui1.show()
    def exit(self):
        self.close()
    def initUI(self):
        self.setWindowTitle("Financial Management")
        self.resize(253, 261)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(60, 70, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 130, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton.clicked.connect(self.signup)
        self.pushButton_2.clicked.connect(self.login)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(-60, 10, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_4 = QtWidgets.QPushButton(self)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 190, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.exit)
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("Dialog", "Sign Up"))
        self.pushButton_2.setText(_translate("Dialog", "Log In"))
        self.label.setText(_translate("Dialog", "        Welcome"))
        self.pushButton_4.setText(_translate("Dialog", "Exit"))
        self.show()

        
      

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = main()
    sys.exit(app.exec_())
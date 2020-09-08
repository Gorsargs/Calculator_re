from PyQt5 import QtCore, QtGui, QtWidgets
from Calculator import Calculator
from time import sleep
from playsound import playsound
import threading


text = ""
endline = False
parcount = 0
dotcount = True

class Ui_Dialog(QtWidgets.QMainWindow):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(504, 489)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\calculator.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 130, 71, 81))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    color: #FFFFFF;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: gray;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: #FFFFFF;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: #535052;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    color: #C7C0C5;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: gray;\n"
"\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 130, 71, 81))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    color: #FFFFFF;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: gray;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: #FFFFFF;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: #535052;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    color: #C7C0C5;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: gray;\n"
"\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 130, 71, 81))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    color: #FFFFFF;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: gray;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: #FFFFFF;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: #535052;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    color: #C7C0C5;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: gray;\n"
"\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 220, 71, 81))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    color: #FFFFFF;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: gray;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: #FFFFFF;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: #535052;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    color: #C7C0C5;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: gray;\n"
"\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(90, 220, 71, 81))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    color: #FFFFFF;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: gray;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: #FFFFFF;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: #535052;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    color: #C7C0C5;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: gray;\n"
"\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(170, 220, 71, 81))
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"    color: #FFFFFF;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: gray;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: #FFFFFF;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: #535052;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    color: #C7C0C5;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: gray;\n"
"\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 310, 71, 81))
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"    color: #FFFFFF;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: gray;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: #FFFFFF;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: #535052;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    color: #C7C0C5;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: gray;\n"
"\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(90, 310, 71, 81))
        self.pushButton_8.setStyleSheet("QPushButton {\n"
"    color: #FFFFFF;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: gray;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: #FFFFFF;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: #535052;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    color: #C7C0C5;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: gray;\n"
"\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(Dialog)
        self.pushButton_9.setGeometry(QtCore.QRect(170, 310, 71, 81))
        self.pushButton_9.setStyleSheet("QPushButton {\n"
"    color: #FFFFFF;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: gray;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: #FFFFFF;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: #535052;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    color: #C7C0C5;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: gray;\n"
"\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_0 = QtWidgets.QPushButton(Dialog)
        self.pushButton_0.setGeometry(QtCore.QRect(10, 400, 71, 81))
        self.pushButton_0.setStyleSheet("QPushButton {\n"
"    color: #FFFFFF;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: gray;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: #FFFFFF;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: #535052;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    color: #C7C0C5;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: gray;\n"
"\n"
"}")
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_equal = QtWidgets.QPushButton(Dialog)
        self.pushButton_equal.setGeometry(QtCore.QRect(90, 400, 151, 81))
        self.pushButton_equal.setStyleSheet("QPushButton {\n"
"    color: #FFFFFF;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: gray;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: #FFFFFF;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: #535052;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    color: #C7C0C5;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: gray;\n"
"\n"
"}")
        self.pushButton_equal.setObjectName("pushButton_equal")
        self.pushButton_increase = QtWidgets.QPushButton(Dialog)
        self.pushButton_increase.setGeometry(QtCore.QRect(420, 130, 71, 81))
        self.pushButton_increase.setStyleSheet("QPushButton {\n"
"    color: #FFFFFF;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: gray;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: #FFFFFF;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: #535052;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    color: #C7C0C5;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: gray;\n"
"\n"
"}")
        self.pushButton_increase.setObjectName("pushButton_increase")
        self.pushButton_devide = QtWidgets.QPushButton(Dialog)
        self.pushButton_devide.setGeometry(QtCore.QRect(340, 130, 71, 81))
        self.pushButton_devide.setStyleSheet("QPushButton {\n"
"    color: #FFFFFF;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: gray;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: #FFFFFF;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: #535052;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    color: #C7C0C5;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: gray;\n"
"\n"
"}")
        self.pushButton_devide.setObjectName("pushButton_devide")
        self.pushButton_multiply = QtWidgets.QPushButton(Dialog)
        self.pushButton_multiply.setGeometry(QtCore.QRect(260, 130, 71, 81))
        self.pushButton_multiply.setStyleSheet("QPushButton {\n"
"    color: #FFFFFF;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: gray;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: #FFFFFF;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: #535052;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    color: #C7C0C5;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: gray;\n"
"\n"
"}")
        self.pushButton_multiply.setObjectName("pushButton_multiply")
        self.pushButton_minus = QtWidgets.QPushButton(Dialog)
        self.pushButton_minus.setGeometry(QtCore.QRect(260, 220, 71, 81))
        self.pushButton_minus.setStyleSheet("QPushButton {\n"
"    color: #FFFFFF;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: gray;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: #FFFFFF;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: #535052;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    color: #C7C0C5;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: gray;\n"
"\n"
"}")
        self.pushButton_minus.setObjectName("pushButton_minus")
        self.pushButton_plus = QtWidgets.QPushButton(Dialog)
        self.pushButton_plus.setGeometry(QtCore.QRect(340, 220, 71, 81))
        self.pushButton_plus.setStyleSheet("QPushButton {\n"
"    color: #FFFFFF;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: gray;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: #FFFFFF;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: #535052;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    color: #C7C0C5;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: gray;\n"
"\n"
"}")
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.pushButton_root = QtWidgets.QPushButton(Dialog)
        self.pushButton_root.setGeometry(QtCore.QRect(420, 220, 71, 81))
        self.pushButton_root.setStyleSheet("QPushButton {\n"
"    color: #FFFFFF;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: gray;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: #FFFFFF;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: #535052;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    color: #C7C0C5;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: gray;\n"
"\n"
"}")
        self.pushButton_root.setObjectName("pushButton_root")
        self.pushButton_parent2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_parent2.setGeometry(QtCore.QRect(420, 310, 71, 81))
        self.pushButton_parent2.setStyleSheet("QPushButton {\n"
"    color: #FFFFFF;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: gray;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: #FFFFFF;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: #535052;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    color: #C7C0C5;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: gray;\n"
"\n"
"}")
        self.pushButton_parent2.setObjectName("pushButton_parent2")
        self.pushButton_parent1 = QtWidgets.QPushButton(Dialog)
        self.pushButton_parent1.setGeometry(QtCore.QRect(340, 310, 71, 81))
        self.pushButton_parent1.setStyleSheet("QPushButton {\n"
"    color: #FFFFFF;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: gray;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: #FFFFFF;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: #535052;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    color: #C7C0C5;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: gray;\n"
"\n"
"}")
        self.pushButton_parent1.setObjectName("pushButton_parent1")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 481, 51))
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("color: #33FFF9;\n"
"font: 28pt \"MS Gothic\";\n"
"background-color: gray;\n"
"\n"
"")
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setCursorPosition(0)
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 70, 481, 51))
        self.lineEdit_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_2.setAutoFillBackground(False)
        self.lineEdit_2.setStyleSheet("color: #33FFFF;\n"
"font: 28pt \"MS Gothic\";\n"
"background-color: grey;\n"
"\n"
"")
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setCursorPosition(0)
        self.lineEdit_2.setDragEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_delete = QtWidgets.QPushButton(Dialog)
        self.pushButton_delete.setGeometry(QtCore.QRect(260, 400, 71, 81))
        self.pushButton_delete.setStyleSheet("QPushButton {\n"
"    color: #FFFFFF;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: gray;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: #FFFFFF;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: #535052;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    color: #C7C0C5;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: gray;\n"
"\n"
"}")
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.pushButton_percent = QtWidgets.QPushButton(Dialog)
        self.pushButton_percent.setGeometry(QtCore.QRect(260, 310, 71, 81))
        self.pushButton_percent.setStyleSheet("QPushButton {\n"
"    color: #FFFFFF;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: gray;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: #FFFFFF;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: #535052;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    color: #C7C0C5;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: gray;\n"
"\n"
"}")
        self.pushButton_percent.setObjectName("pushButton_percent")
        self.pushButton_deleteall = QtWidgets.QPushButton(Dialog)
        self.pushButton_deleteall.setGeometry(QtCore.QRect(340, 400, 71, 81))
        self.pushButton_deleteall.setStyleSheet("QPushButton {\n"
"    color: #FFFFFF;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: gray;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: #FFFFFF;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: #535052;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    color: #C7C0C5;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: gray;\n"
"\n"
"}")
        self.pushButton_deleteall.setObjectName("pushButton_deleteall")
        self.pushButton_imsad = QtWidgets.QPushButton(Dialog)
        self.pushButton_imsad.setGeometry(QtCore.QRect(460, 400, 31, 81))
        self.pushButton_imsad.setStyleSheet("QPushButton {\n"
"    color: #FFFFFF;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: gray;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: #FFFFFF;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: #535052;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    color: #C7C0C5;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: gray;\n"
"\n"
"}")
        self.pushButton_imsad.setObjectName("pushButton_imsad")
        self.pushButton_dot = QtWidgets.QPushButton(Dialog)
        self.pushButton_dot.setGeometry(QtCore.QRect(420, 400, 31, 81))
        self.pushButton_dot.setStyleSheet("QPushButton {\n"
"    color: #FFFFFF;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: gray;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: #FFFFFF;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: #535052;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    color: #C7C0C5;\n"
"    font: 21pt \"Times Unicode\";\n"
"    background-color: gray;\n"
"\n"
"}")
        self.pushButton_dot.setObjectName("pushButton_dot")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton_0.clicked.connect(self.button_presser)
        self.pushButton.clicked.connect(self.button_presser)
        self.pushButton_2.clicked.connect(self.button_presser)
        self.pushButton_3.clicked.connect(self.button_presser)
        self.pushButton_4.clicked.connect(self.button_presser)
        self.pushButton_5.clicked.connect(self.button_presser)
        self.pushButton_6.clicked.connect(self.button_presser)
        self.pushButton_7.clicked.connect(self.button_presser)
        self.pushButton_8.clicked.connect(self.button_presser)
        self.pushButton_9.clicked.connect(self.button_presser)
        self.pushButton_plus.clicked.connect(self.button_press_plus)
        self.pushButton_minus.clicked.connect(self.button_press_minus)
        self.pushButton_multiply.clicked.connect(self.button_press_multiply)
        self.pushButton_devide.clicked.connect(self.button_press_devide)
        self.pushButton_root.clicked.connect(self.button_press_root)
        self.pushButton_increase.clicked.connect(self.button_press_increase)
        self.pushButton_parent1.clicked.connect(self.button_press_parent1)
        self.pushButton_parent2.clicked.connect(self.button_press_parent2)
        self.pushButton_equal.clicked.connect(self.button_press_equal)
        self.pushButton_delete.clicked.connect(self.button_press_delete)
        self.pushButton_imsad.clicked.connect(self.hearts_threaded)
        self.pushButton_deleteall.clicked.connect(self.button_press_deleteall)
        self.pushButton_percent.clicked.connect(self.button_press_percent)
        self.pushButton_dot.clicked.connect(self.button_press_dot)

    def button_presser(self):
        global text
        sender = self.sender()
        text += sender.text()
        self.lineEdit.setText(text)

    def button_press_plus(self):
        global text
        global dotcount
        dotcount = True
        text += self.pushButton_plus.text()
        self.lineEdit.setText(text)

    def button_press_minus(self):
        global text
        global dotcount
        dotcount = True
        text += self.pushButton_minus.text()
        self.lineEdit.setText(text)


    def button_press_multiply(self):
        global text
        global dotcount
        dotcount = True
        text += self.pushButton_multiply.text()
        self.lineEdit.setText(text)

    def button_press_increase(self):
        global parcount
        global text
        global dotcount
        dotcount = True
        text += self.pushButton_increase.text()
        text += self.pushButton_parent1.text()
        parcount += 1
        self.lineEdit.setText(text)

    def button_press_root(self):
        global parcount
        global text
        global dotcount
        dotcount = True
        text += self.pushButton_root.text()
        text += self.pushButton_parent1.text()
        parcount += 1
        self.lineEdit.setText(text)

    def button_press_devide(self):
        global text
        global dotcount
        dotcount = True
        text += self.pushButton_devide.text()
        self.lineEdit.setText(text)

    def button_press_parent1(self):
        global parcount
        global text
        global dotcount
        dotcount = True
        text += self.pushButton_parent1.text()
        parcount += 1
        self.lineEdit.setText(text)

    def button_press_parent2(self):
        global parcount
        global dotcount
        if parcount > 0:
            global text
            text += self.pushButton_parent2.text()
            parcount -= 1
            dotcount = True
            self.lineEdit.setText(text)

    def button_press_equal(self):
        global text
        global parcount
        if text.count("(") > text.count(")"):
            text += (text.count("(") - text.count(")")) * self.pushButton_parent2.text()
            parcount -= text.count(")")
        self.lineEdit.setText(text)
        text1 = Calculator.calculator(text)
        if type(text) == str:
            self.lineEdit_2.setText(text1)
        else:
            text = ""
            self.lineEdit_2.setText(text1)

    def button_press_delete(self):
        global text
        global parcount
        global dotcount
        try:
            if text[-1] == ")":
                parcount += 1
            elif text[-1] == ".":
                dotcount = True
            elif text[-1] == "(":
                parcount -=1
        except:
            pass
        if len(text)>0:
            text = text[:-1:]
        else:
            print("¯¯\_( ͡ .,,. ͡ )_/¯¯")
        self.lineEdit.setText(text)

    def button_press_percent(self):
        global text
        global dotcount
        dotcount = True
        text += self.pushButton_percent.text()
        self.lineEdit.setText(text)

    def button_press_deleteall(self):
        global text
        global dotcount
        text = ""
        self.lineEdit.setText(text)
        self.lineEdit_2.setText(text)
        dotcount = True

    def button_press_dot(self):
        global text
        global dotcount
        if len(text)>0:
            if text[-1] in "0123456789" and dotcount:
                text += self.pushButton_dot.text()
                self.lineEdit.setText(text)
                dotcount = False




        else:
            print("not enough numbers")

    def button_press_imsad(self):
        global text
        text = ""
        for i in range(5):
            text += ":O "
            sleep(1)
            self.lineEdit.setText(text)
        sleep(1)
        text += " virus activated"
        self.lineEdit.setText(text)
        sleep(1)
        text1 = ""
        for i in  "thank you for downloading my program :O ":
            text1 += i
            sleep(0.1)
            self.lineEdit_2.setText(text1)
        text = ""
        self.pushButton_imsad.setText(":)")
        self.pushButton.setText("──")
        sleep(0.5)
        self.pushButton_2.setText("┐")
        sleep(0.5)
        self.pushButton_5.setText("┼")
        sleep(0.5)
        self.pushButton_8.setText("└")
        sleep(0.5)
        self.pushButton_9.setText("──")
        sleep(0.5)
        self.pushButton_7.setText("|")
        sleep(0.5)
        self.pushButton_4.setText("┌")
        sleep(0.5)
        self.pushButton_6.setText("┘")
        sleep(0.5)
        self.pushButton_3.setText("|")
        playsound('.\\soviet.mp3')



    def hearts_threaded(self):
        t = threading.Thread(target=self.button_press_imsad, name="Thread-1", daemon = True)
        t.start()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Calculator"))
        self.pushButton.setText(_translate("Dialog", "1"))
        self.pushButton_2.setText(_translate("Dialog", "2"))
        self.pushButton_3.setText(_translate("Dialog", "3"))
        self.pushButton_4.setText(_translate("Dialog", "4"))
        self.pushButton_5.setText(_translate("Dialog", "5"))
        self.pushButton_6.setText(_translate("Dialog", "6"))
        self.pushButton_7.setText(_translate("Dialog", "7"))
        self.pushButton_8.setText(_translate("Dialog", "8"))
        self.pushButton_9.setText(_translate("Dialog", "9"))
        self.pushButton_0.setText(_translate("Dialog", "0"))
        self.pushButton_equal.setText(_translate("Dialog", "="))
        self.pushButton_increase.setText(_translate("Dialog", "^"))
        self.pushButton_devide.setText(_translate("Dialog", "/"))
        self.pushButton_multiply.setText(_translate("Dialog", "*"))
        self.pushButton_minus.setText(_translate("Dialog", "-"))
        self.pushButton_plus.setText(_translate("Dialog", "+"))
        self.pushButton_root.setText(_translate("Dialog", "√"))
        self.pushButton_parent2.setText(_translate("Dialog", ")"))
        self.pushButton_parent1.setText(_translate("Dialog", "("))
        self.pushButton_delete.setText(_translate("Dialog", "C"))
        self.pushButton_percent.setText(_translate("Dialog", "%"))
        self.pushButton_deleteall.setText(_translate("Dialog", "CE"))
        self.pushButton_imsad.setText(_translate("Dialog", ":("))
        self.pushButton_dot.setText(_translate("Dialog", "."))

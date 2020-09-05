import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from test import Ui_Dialog
from Calculator import Calculator
from time import sleep
import threading
from playsound import playsound

app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()

ui = Ui_Dialog()
ui.setupUi(Dialog)

text = ""
endline = False
parcount = 0
dotcount = True



Dialog.show()


def button_press_0():
    global text
    text += ui.pushButton_0.text()
    ui.lineEdit.setText(text)

def button_press():
    global text
    text += ui.pushButton.text()
    number = True
    ui.lineEdit.setText(text)

def button_press_2():
    global text
    text += ui.pushButton_2.text()
    ui.lineEdit.setText(text)

def button_press_3():
    global text
    text += ui.pushButton_3.text()
    ui.lineEdit.setText(text)

def button_press_4():
    global text
    text += ui.pushButton_4.text()
    ui.lineEdit.setText(text)

def button_press_5():
    global text
    text += ui.pushButton_5.text()
    ui.lineEdit.setText(text)

def button_press_6():
    global text
    text += ui.pushButton_6.text()
    ui.lineEdit.setText(text)

def button_press_7():
    global text
    text += ui.pushButton_7.text()
    ui.lineEdit.setText(text)

def button_press_8():
    global text
    text += ui.pushButton_8.text()
    ui.lineEdit.setText(text)

def button_press_9():
    global text
    text += ui.pushButton_9.text()
    ui.lineEdit.setText(text)

def button_press_plus():
    global text
    global dotcount
    dotcount = True
    text += ui.pushButton_plus.text()
    ui.lineEdit.setText(text)

def button_press_minus():
    global text
    global dotcount
    dotcount = True
    text += ui.pushButton_minus.text()
    ui.lineEdit.setText(text)


def button_press_multiply():
    global text
    global dotcount
    dotcount = True
    text += ui.pushButton_multiply.text()
    ui.lineEdit.setText(text)

def button_press_increase():
    global parcount
    global text
    global dotcount
    dotcount = True
    text += ui.pushButton_increase.text()
    text += ui.pushButton_parent1.text()
    parcount += 1
    ui.lineEdit.setText(text)

def button_press_root():
    global parcount
    global text
    global dotcount
    dotcount = True
    text += ui.pushButton_root.text()
    text += ui.pushButton_parent1.text()
    parcount += 1
    ui.lineEdit.setText(text)

def button_press_devide():
    global text
    global dotcount
    dotcount = True
    text += ui.pushButton_devide.text()
    ui.lineEdit.setText(text)

def button_press_parent1():
    global parcount
    global text
    global dotcount
    dotcount = True
    text += ui.pushButton_parent1.text()
    parcount += 1
    ui.lineEdit.setText(text)

def button_press_parent2():
    global parcount
    global dotcount
    if parcount > 0:
        global text
        text += ui.pushButton_parent2.text()
        parcount -= 1
        dotcount = True
        ui.lineEdit.setText(text)

def button_press_equal():
    global text
    if text.count("(") > text.count(")"):
        text += (text.count("(") - text.count(")")) * ")"
    ui.lineEdit.setText(text)
    text1 = Calculator.calculator(text)
    if type(text) == str:
        ui.lineEdit_2.setText(text1)
    else:
        text = ""
        ui.lineEdit_2.setText(text1)

def button_press_delete():
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
    ui.lineEdit.setText(text)

def button_press_percent():
    global text
    global dotcount
    dotcount = True
    text += ui.pushButton_percent.text()
    ui.lineEdit.setText(text)

def button_press_deleteall():
    global text
    global dotcount
    text = ""
    ui.lineEdit.setText(text)
    ui.lineEdit_2.setText(text)
    dotcount = True

def button_press_dot():
    global text
    global dotcount
    if len(text)>0:
        if text[-1] in "0123456789" and dotcount:
            text += ui.pushButton_dot.text()
            ui.lineEdit.setText(text)
            dotcount = False




    else:
        print("not enough numbers")

def button_press_imsad():
    global text
    text = ""
    for i in range(5):
        text += ":O "
        sleep(1)
        ui.lineEdit.setText(text)
    sleep(1)
    text += " virus activated"
    ui.lineEdit.setText(text)
    sleep(1)
    text1 = ""
    for i in  "thank you for downloading my program :O ":
        text1 += i
        sleep(0.1)
        ui.lineEdit_2.setText(text1)
    text = ""
    ui.pushButton_imsad.setText(":)")
    ui.pushButton.setText("──")
    sleep(0.5)
    ui.pushButton_2.setText("┐")
    sleep(0.5)
    ui.pushButton_5.setText("┼")
    sleep(0.5)
    ui.pushButton_8.setText("└")
    sleep(0.5)
    ui.pushButton_9.setText("──")
    sleep(0.5)
    ui.pushButton_7.setText("|")
    sleep(0.5)
    ui.pushButton_4.setText("┌")
    sleep(0.5)
    ui.pushButton_6.setText("┘")
    sleep(0.5)
    ui.pushButton_3.setText("|")
    playsound('soviet.mp3')


def hearts_threaded():
    t = threading.Thread(target=button_press_imsad, name="Thread-1")
    t.start()





ui.pushButton_0.clicked.connect(button_press_0)
ui.pushButton.clicked.connect(button_press)
ui.pushButton_2.clicked.connect(button_press_2)
ui.pushButton_3.clicked.connect(button_press_3)
ui.pushButton_4.clicked.connect(button_press_4)
ui.pushButton_5.clicked.connect(button_press_5)
ui.pushButton_6.clicked.connect(button_press_6)
ui.pushButton_7.clicked.connect(button_press_7)
ui.pushButton_8.clicked.connect(button_press_8)
ui.pushButton_9.clicked.connect(button_press_9)
ui.pushButton_plus.clicked.connect(button_press_plus)
ui.pushButton_minus.clicked.connect(button_press_minus)
ui.pushButton_multiply.clicked.connect(button_press_multiply)
ui.pushButton_devide.clicked.connect(button_press_devide)
ui.pushButton_root.clicked.connect(button_press_root)
ui.pushButton_increase.clicked.connect(button_press_increase)
ui.pushButton_parent1.clicked.connect(button_press_parent1)
ui.pushButton_parent2.clicked.connect(button_press_parent2)
ui.pushButton_equal.clicked.connect(button_press_equal)
ui.pushButton_delete.clicked.connect(button_press_delete)
ui.pushButton_imsad.clicked.connect(hearts_threaded)
ui.pushButton_deleteall.clicked.connect(button_press_deleteall)
ui.pushButton_percent.clicked.connect(button_press_percent)
ui.pushButton_dot.clicked.connect(button_press_dot)
sys.exit(app.exec_())

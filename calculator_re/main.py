import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_Dialog


app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)


#Main loop
Dialog.show()

sys.exit(app.exec_())

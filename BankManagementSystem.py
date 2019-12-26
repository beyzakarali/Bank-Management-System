from ViewBMS.Giris import Ui_LogIn
import mysql.connector 
from PyQt5 import QtWidgets

def main():
    import sys

    app = QtWidgets.QApplication(sys.argv)
    BMS = Ui_LogIn()
    sys.exit(app.exec_())

main()

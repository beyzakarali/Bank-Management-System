from ViewBMS.Giris import Ui_LOGIN
import mysql.connector 
from PyQt5 import QtWidgets

def main():
    import sys

    app = QtWidgets.QApplication(sys.argv)
    BMS = Ui_LOGIN()
    sys.exit(app.exec_())

main()

##
# KEIMYUNG PROJECT, 2021
# 3DViewer
# File description:
# main
##

# --- IMPORTS ---

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication
from src.Ui.Ui import Ui



        
class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui(self)
        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.ui.BoxFilled())
        self.setCentralWidget(self.mainWidget)
        self.setWindowTitle("BWC Project")
        self.setGeometry(0, 0, 1500, 1000)


        
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("fusion")

    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
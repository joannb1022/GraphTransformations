from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import *
import sys
from random import randint
import TIAAAG
import statistics
import networkx as nx

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.initUI()
        self.showMaximized()

    def initUI(self):

        self.setGeometry(500, 500, 800, 600)
        self.setWindowTitle("Produckje grafu")

        self.image = QtWidgets.QLabel(self)
        self.image.setPixmap(QPixmap("G.png"))
        self.image.setFixedSize(512, 384)
        self.image.move(10, 70)

        self.comboProductions=QtWidgets.QComboBox(self)
        production_list = ["Produkcja 1", "Produkcja 2", "Produkcja 3", "Produkcja 4"]
        self.comboProductions.setGeometry(200, 150, 200, 50)
        self.comboProductions.setEditable(True)
        self.comboProductions.addItems(production_list)
        self.comboProductions.adjustSize()
        self.comboProductions.move(100, 550)
        self.comboProductions.lineEdit().setReadOnly(True)
        self.comboProductions.activated[str].connect(self.onActivated)


        self.textbox = QLineEdit(self)
        self.textbox.move(550, 20)
        self.textbox.resize(380,40)
        self.textbox.setText("Liczba wierzchołków jest równa: 5") #to trzeba ładniej na pewno, zeby było uniwersalne, niezaleznie jaki graf wejsciowy


    def onActivated(self, text):
        for s in text.split():
            if s.isdigit():
                G = TIAAAG.production_gui(int(s))
                if G is not None:
                    self.image.setPixmap(QPixmap("G1.png"))
                    self.textbox.setText("Liczba wierzchołków jest równa: " + str(statistics.nodes_gui(G))) #nie wiem, jak inaczej niz zmienic fnkcje get_stats na takie pojedyncze


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()

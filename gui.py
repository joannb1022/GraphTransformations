import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *

import globals
import production
import statistics
from parsing import parse_input


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.legendtext = QLabel(self)
        self.legend = QtWidgets.QLabel(self)
        self.textbox = QLabel(self)
        self.comboProductions = QtWidgets.QComboBox(self)
        self.image = QtWidgets.QLabel(self)
        self.combolabel = QLabel(self)
        self.inputlabel = QLabel(self)
        self.input = QLineEdit(self)
        self.inputbutton = QPushButton(self)
        self.initUI()
        self.showMaximized()

    def initUI(self):

        self.setGeometry(500, 500, 800, 600)
        self.setWindowTitle("Transformacje grafowe")

        # Drawing and displaying initial graph
        statistics.draw(globals.G, [], [], [], [], "G.png")
        self.image.setPixmap(QPixmap("G.png"))
        self.image.setFixedSize(512, 384)
        self.image.move(10, 50)
        self.image.setStyleSheet("border: 1px solid black")

        # Getting list of productions and creating ComboBox of productions
        production_list = production.get_productions_list()
        self.comboProductions.setGeometry(200, 150, 200, 50)
        self.comboProductions.setEditable(True)
        self.comboProductions.addItems(production_list)
        self.comboProductions.adjustSize()
        self.comboProductions.move(220, 540)
        self.comboProductions.lineEdit().setReadOnly(True)
        self.comboProductions.activated[str].connect(self.onActivatedComboBox)

        # Text label with results of production, initialized with initial graph statistics
        self.textbox.move(550, 50)
        self.textbox.resize(300, 110)
        self.textbox.setStyleSheet("border: 1px solid black")
        self.textbox.setText(statistics.get_stats(globals.G))

        # Text label for ComboBox
        self.combolabel.move(50, 535)
        self.combolabel.resize(150, 20)
        self.combolabel.setText("Wybierz produkcję z listy ")

        # Text label for input
        self.inputlabel.move(50, 440)
        self.inputlabel.resize(150, 80)
        self.inputlabel.setText("Podaj ciąg produkcji oddzielony \nprzecinkami (np. 1,2,10,12) \n\n\n lub")

        # Input field
        self.input.move(220, 450)
        self.input.resize(150, 30)

        # Input button
        self.inputbutton.move(390, 450)
        self.inputbutton.setText("Wykonaj")
        self.inputbutton.clicked.connect(self.onActivatedInput)

        # Legend of the usage of colors in graph representation
        self.legend.setPixmap(QPixmap("data/legend.png"))
        self.legend.setFixedSize(50, 120)
        self.legend.move(600, 200)

        self.legendtext.move(660, 200)
        self.legendtext.resize(300, 115)
        self.legendtext.setText(" - prawa strona produkcji\n\n\n - nowe krawędzie\n\n\n - pozostałe węzły")

    # Performing production when chosen from ComboBox
    def onActivatedComboBox(self, text):
        for s in text.split():
            if s.isdigit():
                self.display_productions([int(s)])

    # Attempt to perform and display productions and statistics
    def display_productions(self, prod_nr):
        for i in prod_nr:
            if i < 1 or i > globals.N:
                self.textbox.setText(
                    "Produkcja {} nie może być zrealizowana. \n\n  Produkcja nie istnieje".format(i))
                continue
            newG = production.production(i)
            if newG is not None:
                globals.G = newG
                self.image.setPixmap(QPixmap("G1.png"))
                self.textbox.setText(statistics.get_stats(globals.G))
            else:
                self.textbox.setText(
                    "Produkcja {} nie może być zrealizowana. \n\n  W grafie początkowym nie znaleziono "
                    "wierzchołka\n  lewej strony produkcji".format(i))

    # Parsing input and performing productions
    def onActivatedInput(self):
        input = self.input.text()
        prod_nr = parse_input(input)
        if prod_nr:
            self.display_productions(prod_nr)
        else:
            self.textbox.setText(
                "Produkcja nie może być zrealizowana. \n\n Błędne dane wejściowe.")
        self.input.clear()


# Displaying window
def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

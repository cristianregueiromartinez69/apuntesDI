import sys

from PyQt6.QtWidgets import QMainWindow, QTabWidget, QVBoxLayout, QWidget, QApplication

from view.tabpokedex.Pokedex import Pokedex
from view.tabpokedexlist.PokedexList import PokedexList
from view.tabpokedextable.PokedexTableView import PokedexTable


class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pokedex")
        self.setFixedSize(900, 750)

        self.tab_widget = QTabWidget()
        self.layout_principal = QVBoxLayout()



        self.pokedex = Pokedex()
        self.pokedex_list = PokedexList()
        self.pokkedex_table = PokedexTable()

        self.tab_widget.addTab(self.pokedex, "Pokedex")
        self.tab_widget.addTab(self.pokedex_list, "Lista POkedex")
        self.tab_widget.addTab(self.pokkedex_table, "Tabla Pokedex")

        self.layout_principal.addWidget(self.tab_widget)

        container = QWidget()
        container.setLayout(self.layout_principal)

        self.setCentralWidget(container)

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    app.exec()


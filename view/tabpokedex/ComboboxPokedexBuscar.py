import sys

from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTabWidget, QFrame,
                             QGridLayout, QComboBox, QPushButton)

class ComboBoxPokedexBuscar(QHBoxLayout):
    def __init__(self):
        super().__init__()

        self.combo_pokemons = QComboBox()
        self.boton_buscar_pokemons_combo = QPushButton("search")

        self.addWidget(self.combo_pokemons)
        self.addWidget(self.boton_buscar_pokemons_combo)
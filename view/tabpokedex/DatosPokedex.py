import sys

from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTabWidget, QLayout,
                             QGridLayout, QLabel, QLineEdit)


class DatosPokedex(QGridLayout):
    def __init__(self):
        super().__init__()

        self.label_nombre_pokemon = QLabel("Name: ")
        self.label_type_pokemon = QLabel("Type: ")
        self.label_hp_pokemon = QLabel("HP: ")
        self.label_attack_pokemon = QLabel("Attack: ")
        self.label_defense_pokemon = QLabel("Defense: ")
        self.label_sp_attack_pokemon = QLabel("Sp. Attack: ")
        self.label_sp_defense_pokemon = QLabel("Sp. Defense: ")
        self.label_speed_pokemon = QLabel("Speed: ")

        self.txt_nombre_pokemon = QLineEdit()
        self.txt_type_pokemon = QLineEdit()
        self.txt_hp_pokemon = QLineEdit()
        self.txt_attack_pokemon = QLineEdit()
        self.txt_defense_pokemon = QLineEdit()
        self.txt_sp_attack_pokemon = QLineEdit()
        self.txt_sp_defense_pokemon = QLineEdit()
        self.txt_speed_pokemon = QLineEdit()

        self.txt_nombre_pokemon.setReadOnly(True)
        self.txt_type_pokemon.setReadOnly(True)
        self.txt_hp_pokemon.setReadOnly(True)
        self.txt_attack_pokemon.setReadOnly(True)
        self.txt_defense_pokemon.setReadOnly(True)
        self.txt_sp_attack_pokemon.setReadOnly(True)
        self.txt_sp_defense_pokemon.setReadOnly(True)
        self.txt_speed_pokemon.setReadOnly(True)

        self.addWidget(self.label_nombre_pokemon, 0, 0, 1, 1)
        self.addWidget(self.label_type_pokemon, 1, 0, 1, 1)
        self.addWidget(self.label_hp_pokemon, 2, 0, 1, 1)
        self.addWidget(self.label_attack_pokemon, 3, 0, 1, 1)
        self.addWidget(self.label_defense_pokemon, 4, 0, 1, 1)
        self.addWidget(self.label_sp_attack_pokemon, 5, 0, 1, 1)
        self.addWidget(self.label_sp_defense_pokemon, 6, 0, 1, 1)
        self.addWidget(self.label_speed_pokemon, 7, 0, 1, 1)

        self.addWidget(self.txt_nombre_pokemon, 0, 1, 1, 1)
        self.addWidget(self.txt_type_pokemon, 1, 1, 1, 1)
        self.addWidget(self.txt_hp_pokemon, 2, 1, 1, 1)
        self.addWidget(self.txt_attack_pokemon, 3, 1, 1, 1)
        self.addWidget(self.txt_defense_pokemon, 4, 1, 1, 1)
        self.addWidget(self.txt_sp_attack_pokemon, 5, 1, 1, 1)
        self.addWidget(self.txt_sp_defense_pokemon, 6, 1, 1, 1)
        self.addWidget(self.txt_speed_pokemon, 7, 1, 1, 1)




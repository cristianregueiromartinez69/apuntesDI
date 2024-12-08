import sys

from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTabWidget, QFrame,
                             QGridLayout, QTableView, QLabel, QLineEdit)


class DatosCrud(QGridLayout):
    def __init__(self):
        super().__init__()

        self.label_name_tabla = QLabel("Name")
        self.label_type_tabla = QLabel("Type")
        self.label_hp_tabla = QLabel("HP")
        self.label_attack_tabla = QLabel("Attack")
        self.label_defense_tabla = QLabel("Defense")
        self.label_spattack_tabla = QLabel("Sp.Attack")
        self.label_spedefense_tabla = QLabel("Sp.Defense")
        self.label_speed_tabla = QLabel("Speed")

        self.txt_name_tabla = QLineEdit()
        self.txt_type_tabla = QLineEdit()
        self.txt_hp_tabla = QLineEdit()
        self.txt_attack_tabla = QLineEdit()
        self.txt_defense_tabla = QLineEdit()
        self.txt_spattack_tabla = QLineEdit()
        self.txt_spedefense_tabla = QLineEdit()
        self.txt_speed_tabla = QLineEdit()

        self.txt_name_tabla.setPlaceholderText("nombre del pokemon aquí...")
        self.txt_type_tabla.setPlaceholderText("tipo del pokemon aquí...")
        self.txt_hp_tabla.setPlaceholderText("vida del pokemon aquí...")
        self.txt_attack_tabla.setPlaceholderText("ataque del pokemon aquí...")
        self.txt_defense_tabla.setPlaceholderText("defensa del pokemon aquí...")
        self.txt_spattack_tabla.setPlaceholderText("ataque especial del pokemon aquí...")
        self.txt_spedefense_tabla.setPlaceholderText("defensa especial del pokemon aquí...")
        self.txt_speed_tabla.setPlaceholderText("velocidad del pokemon aquí...")

        self.addWidget(self.label_name_tabla, 0, 0, 1, 1)
        self.addWidget(self.txt_name_tabla, 0, 1, 1, 1)

        self.addWidget(self.label_type_tabla, 1, 0, 1, 1)
        self.addWidget(self.txt_type_tabla, 1, 1, 1, 1)

        self.addWidget(self.label_hp_tabla, 2, 0, 1, 1)
        self.addWidget(self.txt_hp_tabla, 2, 1, 1, 1)

        self.addWidget(self.label_attack_tabla, 3, 0, 1, 1)
        self.addWidget(self.txt_attack_tabla, 3, 1, 1, 1)

        self.addWidget(self.label_defense_tabla, 4, 0, 1, 1)
        self.addWidget(self.txt_defense_tabla, 4, 1, 1, 1)

        self.addWidget(self.label_spattack_tabla, 5, 0, 1, 1)
        self.addWidget(self.txt_spattack_tabla, 5, 1, 1, 1)

        self.addWidget(self.label_spedefense_tabla, 6, 0, 1, 1)
        self.addWidget(self.txt_spedefense_tabla, 6, 1, 1, 1)

        self.addWidget(self.label_speed_tabla, 7, 0, 1, 1)
        self.addWidget(self.txt_speed_tabla, 7, 1, 1, 1)

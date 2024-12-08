import sys

from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTabWidget, QFrame,
                             QGridLayout, QTableView, QLabel, QLineEdit, QPushButton)

class BotonesCrud(QVBoxLayout):
    def __init__(self):
        super().__init__()

        self.botton_inserccion = QPushButton("Insertar")
        self.botton_actualizar = QPushButton("Actualizar")
        self.boton_borrar = QPushButton("Borrar")

        self.botton_inserccion.setStyleSheet("background-color: cyan;")
        self.botton_actualizar.setStyleSheet("background-color: yellow;")
        self.boton_borrar.setStyleSheet("background-color: red;")




        self.caja_horizontal_botones_crud = QHBoxLayout()
        self.caja_horizontal_botones_crud.addWidget(self.botton_inserccion)
        self.caja_horizontal_botones_crud.addWidget(self.botton_actualizar)
        self.caja_horizontal_botones_crud.addWidget(self.boton_borrar)



        self.addLayout(self.caja_horizontal_botones_crud)

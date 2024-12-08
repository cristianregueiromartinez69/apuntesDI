from PyQt6.QtWidgets import QHBoxLayout, QPushButton


class Buttons(QHBoxLayout):
    def __init__(self):
        super().__init__()
        self.boton_borrar = QPushButton("Delete")
        self.boton_añadir = QPushButton("Complete")

        self.addWidget(self.boton_borrar)
        self.addWidget(self.boton_añadir)
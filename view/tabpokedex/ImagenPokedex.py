import sys
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

class ImagenPokedex(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.imagen_label = QLabel()

        pixmap = QPixmap("C:/Users/crm23/Downloads/pokedex.png")

        self.imagen_label.setPixmap(pixmap)

        self.imagen_label.setScaledContents(True)

        layout.addWidget(self.imagen_label)

        self.setLayout(layout)
from PyQt6.QtWidgets import QHBoxLayout, QLineEdit


class TextoLista(QHBoxLayout):
    def __init__(self):
        super().__init__()

        self.texto = QLineEdit()
        self.texto.setPlaceholderText('Añade algo...')
        self.addWidget(self.texto)
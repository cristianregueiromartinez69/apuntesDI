import sys

from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTabWidget, QFrame,
                             QGridLayout, QListView, QPushButton)

from view.tabpokedexlist.BotonesAñadir import Buttons
from view.tabpokedexlist.TextoLista import TextoLista
from model.modellista.QListModel import ModeloTareas


class PokedexList(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PokedexList")
        self.setFixedSize(600, 600)

        # Crear una lista de tareas
        self.tareas = [
            (False, "Estudiar DI"),
            (True, "Estudiar PMDM"),
            (False, "Mirar netflix"),
            (True, "mirar futbol"),
            (False, "hacer examen de PMDM"),
            (True, "morirme")

        ]

        # Crear el modelo
        self.modelo = ModeloTareas(self.tareas)

        # Crear la vista
        self.lista_vista = QListView()
        self.lista_vista.setModel(self.modelo)
        self.lista_vista.setSelectionMode(QListView.SelectionMode.MultiSelection)

        # Crear un layout y agregar la vista
        self.layout = QVBoxLayout()
        self.layoutButton = Buttons()
        self.layoutTexto = TextoLista()
        self.bottonAddList = QPushButton("Add TODO")

        self.layoutButton.boton_añadir.clicked.connect(self.on_button_accept)
        self.layoutButton.boton_borrar.clicked.connect(self.on_button_borrar)
        self.bottonAddList.clicked.connect(self.on_botton_add_list)
        self.layout.addWidget(self.lista_vista)
        self.layout.addLayout(self.layoutButton)
        self.layout.addLayout(self.layoutTexto)
        self.layout.addWidget(self.bottonAddList)

        self.setLayout(self.layout)

    def on_button_accept(self):
        indices = self.lista_vista.selectedIndexes()

        if indices:
            for i in indices:
                _, texto = self.modelo.tarefas[i.row()]
                self.modelo.tarefas[i.row()] = (True, texto)
                self.modelo.dataChanged.emit(i, i)

            self.lista_vista.clearSelection()

    def on_button_borrar(self):
        indices = self.lista_vista.selectedIndexes()
        if indices:
            for i in sorted(indices, reverse=True):
                del self.modelo.tarefas[i.row()]

            self.modelo.layoutChanged.emit()
            self.lista_vista.clearSelection()

    def on_botton_add_list(self):
        texto_añadir = self.layoutTexto.texto.text().strip()
        if texto_añadir:
            self.modelo.tarefas.append((False, texto_añadir))
            self.modelo.layoutChanged.emit()
            self.layoutTexto.texto.clear()

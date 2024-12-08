import sys

from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTabWidget, QFrame,
                             QGridLayout, QTableView)
from PyQt6.sip import delete

from model.modelotabla.ModeloTabla import ModeloTabla
from model.db.ConexionDB import ConexionBD
from view.tabpokedextable.DatosCrudTabla import DatosCrud
from view.tabpokedextable.BotonesCrud import BotonesCrud


class PokedexTable(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pokedex Tabla")
        self.setFixedSize(700, 700)
        self.base = ConexionBD("pokemon.db")
        self.datos = self.base.consultaSenParametros("SELECT * FROM pokemon")

        #layouts
        self.caja_vertical = QVBoxLayout()
        self.tabla_view = QTableView()
        self.datos_crud = DatosCrud()
        self.botones_crud = BotonesCrud()

        #conexiones
        self.botones_crud.botton_inserccion.clicked.connect(self.inserccion_pokemon)
        self.tabla_view.clicked.connect(self.on_cell_clicked)
        self.botones_crud.boton_borrar.clicked.connect(self.delete_pokemon)
        self.botones_crud.botton_actualizar.clicked.connect(self.update_pokemon)


        #tabla
        self.modelo = ModeloTabla(self.datos) if self.datos else ModeloTabla()
        self.tabla_view.setModel(self.modelo)
        self.tabla_view.setSelectionMode(QTableView.SelectionMode.SingleSelection)
        self.cabecera = self.tabla_view.horizontalHeader()

        self.caja_vertical.addWidget(self.tabla_view)
        self.caja_vertical.addLayout(self.datos_crud)
        self.caja_vertical.addLayout(self.botones_crud)

        self.setLayout(self.caja_vertical)

    def inserccion_pokemon(self):
        if self.datos_crud.txt_name_tabla == "" or self.datos_crud.txt_type_tabla == "" or self.datos_crud.txt_hp_tabla == "" or self.datos_crud.txt_attack_tabla == "" or self.datos_crud.txt_defense_tabla == "" or self.datos_crud.txt_spattack_tabla == "" or self.datos_crud.txt_spedefense_tabla == "" or self.datos_crud.txt_speed_tabla == "":
            print("Introduce los datos restantes de los pokemon")
        else:
            nuevo_pokemon = (
                self.datos_crud.txt_name_tabla.text(),
                self.datos_crud.txt_type_tabla.text(),
                self.datos_crud.txt_hp_tabla.text(),
                self.datos_crud.txt_attack_tabla.text(),
                self.datos_crud.txt_defense_tabla.text(),
                self.datos_crud.txt_spattack_tabla.text(),
                self.datos_crud.txt_spedefense_tabla.text(),
                self.datos_crud.txt_speed_tabla.text()
            )
            self.base.insertar_pokemon_uno(nuevo_pokemon)
            self.modelo.tabla.append(nuevo_pokemon)
            self.limpiar_campos_datos_crud()
            self.modelo.layoutChanged.emit()

    def on_cell_clicked(self, index):
        """Guarda la fila seleccionada al hacer clic en una celda."""
        self.selected_row = index.row()  # Almacena la fila seleccionada

    def update_pokemon(self):
        """Actualiza la vida (HP) de un Pokémon seleccionado en la tabla."""
        try:
            # Obtener la fila seleccionada
            indices = self.tabla_view.selectedIndexes()
            if not indices:
                print("No hay ninguna fila seleccionada para actualizar.")
                return

            fila = indices[0].row()  # Obtenemos la fila seleccionada
            if not self.datos_crud.txt_hp_tabla.text():
                print("Introduce un valor para actualizar la vida del Pokémon.")
                return

            # Obtener el nuevo valor de vida
            nueva_vida = self.datos_crud.txt_hp_tabla.text()

            # Actualizar en la base de datos
            clave_original = self.modelo.tabla[fila][0]  # Clave primaria (nombre original)
            self.base.update_pokemons(nueva_vida, clave_original)

            # Crear una nueva tupla con la vida actualizada
            pokemon_actualizado = (
                self.modelo.tabla[fila][0],  # Name
                self.modelo.tabla[fila][1],  # Type
                nueva_vida,  # Actualizar HP
                *self.modelo.tabla[fila][3:]  # Los demás valores permanecen igual
            )

            # Reemplazar la tupla en la tabla del modelo
            self.modelo.tabla[fila] = pokemon_actualizado
            self.modelo.layoutChanged.emit()

            # Limpiar los campos
            self.limpiar_campos_datos_crud()
            print(f"Pokémon '{clave_original}' actualizado correctamente.")
        except Exception as e:
            print(f"Error al actualizar el Pokémon: {e}")

    def delete_pokemon(self):
        """Elimina el Pokémon seleccionado."""
        try:
            # Asegúrate de que hay una fila seleccionada
            if hasattr(self, 'selected_row') and self.selected_row is not None:
                fila = self.selected_row
                datos_fila = self.modelo.tabla[fila]
                clave = datos_fila[0]  # El campo 'name', que es la clave primaria

                # Elimina el Pokémon de la base de datos
                self.base.delete_pokemon(clave)

                # Elimina la fila del modelo de la tabla
                del self.modelo.tabla[fila]

                # Limpia la selección y actualiza la vista
                self.selected_row = None
                self.modelo.layoutChanged.emit()
                print(f"Pokémon '{clave}' eliminado correctamente.")
            else:
                print("No hay ninguna fila seleccionada para eliminar.")
        except IndexError:
            print("Error: La fila seleccionada no existe.")
        except Exception as e:
            print(f"Error inesperado al eliminar el Pokémon: {e}")



    def limpiar_campos_datos_crud(self):
        self.datos_crud.txt_name_tabla.clear()
        self.datos_crud.txt_type_tabla.clear()
        self.datos_crud.txt_hp_tabla.clear()
        self.datos_crud.txt_attack_tabla.clear()
        self.datos_crud.txt_defense_tabla.clear()
        self.datos_crud.txt_spattack_tabla.clear()
        self.datos_crud.txt_spedefense_tabla.clear()
        self.datos_crud.txt_speed_tabla.clear()










import sys

from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTabWidget, QFrame,
                             QGridLayout)

from view.tabpokedex.ComboboxPokedexBuscar import ComboBoxPokedexBuscar
from view.tabpokedex.DatosPokedex import DatosPokedex
from view.tabpokedex.ImagenPokedex import ImagenPokedex
from model.db.ConexionDB import ConexionBD

class Pokedex(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pokedex")
        self.setFixedSize(600, 600)

        #combo y buscar
        self.combo_buscar = ComboBoxPokedexBuscar()
        self.datos_pokedex = DatosPokedex()
        self.imagen = ImagenPokedex()

        # base de datos
        self.base = ConexionBD("C:/Users/crm23/OneDrive/Escritorio/dam2Clase/Desarrollo de Interfaces/apuntesExamen/apuntes2ExamenDI/pokemon.db")


        #funcionalidad combobox
        self.combo_buscar.combo_pokemons.addItems(self.listar_nombres())

        #conexiones
        self.combo_buscar.boton_buscar_pokemons_combo.clicked.connect(self.put_values_pokedex)



        #layouts
        self.layout_principal = QVBoxLayout()

        self.layout_principal.addLayout(self.combo_buscar)
        self.layout_principal.addWidget(self.imagen)
        self.layout_principal.addLayout(self.datos_pokedex)

        
        self.setLayout(self.layout_principal)

    def insertar_datos(self):
        datos_pokemon = [
            ('Pikachu', 'Electric', 35, 55, 40, 50, 50, 90),
            ('Charmander', 'Fire', 39, 52, 43, 60, 50, 65),
            ('Bulbasaur', 'Grass/Poison', 45, 49, 49, 65, 65, 45),
            ('Squirtle', 'Water', 44, 48, 65, 50, 64, 43),
            ('Jigglypuff', 'Normal/Fairy', 115, 45, 20, 45, 25, 20),
            ('Gengar', 'Ghost/Poison', 60, 65, 60, 130, 75, 110),
            ('Onix', 'Rock/Ground', 35, 45, 160, 30, 45, 70),
            ('Alakazam', 'Psychic', 55, 50, 45, 135, 95, 120),
            ('Snorlax', 'Normal', 160, 110, 65, 65, 110, 30),
            ('Dragonite', 'Dragon/Flying', 91, 134, 95, 100, 100, 80)
        ]

        self.base.insertar_pokemon_muchos(datos_pokemon)

    def listar_nombres(self):
        nombres = self.base.consultaSenParametros("SELECT name FROM pokemon")
        if nombres:
            return [nombre[0] for nombre in nombres]
        else:
            return []

    def mostrarDatos(self):
        nombre_pokemon = self.combo_buscar.combo_pokemons.currentText()
        consultaSQl = "SELECT * FROM pokemon WHERE name = ?"
        resultados = self.base.consultaConParametros(consultaSQl, (nombre_pokemon,))
        self.aux_mostrar_datos(resultados)


    def aux_mostrar_datos(self, resultados):
        if resultados:
            pokemon_data = resultados[0]
            self.datos_pokedex.txt_nombre_pokemon.setText(pokemon_data[0])
            self.datos_pokedex.txt_type_pokemon.setText(pokemon_data[1])  
            self.datos_pokedex.txt_hp_pokemon.setText(str(pokemon_data[2])) 
            self.datos_pokedex.txt_attack_pokemon.setText(str(pokemon_data[3]))  
            self.datos_pokedex.txt_defense_pokemon.setText(str(pokemon_data[4]))  
            self.datos_pokedex.txt_sp_attack_pokemon.setText(str(pokemon_data[5]))  
            self.datos_pokedex.txt_sp_defense_pokemon.setText(str(pokemon_data[6]))  
            self.datos_pokedex.txt_speed_pokemon.setText(str(pokemon_data[7]))  
        else:
            # Si no hay resultados (por si no se encuentra el Pokémon)
            print("Pokémon no encontrado.")
            
    def put_values_pokedex(self):
        if self.combo_buscar.combo_pokemons.currentIndex() != -1:
            self.mostrarDatos()















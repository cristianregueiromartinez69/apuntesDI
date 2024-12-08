import sqlite3

class ConexionBD:
    _conexion_compartida = None  # Atributo de clase para mantener una conexión compartida

    def __init__(self, rutaBd):
        """
        Inicializa la conexión a la base de datos. Si ya existe una conexión,
        reutiliza esa conexión en lugar de crear una nueva.
        """
        self.rutaBd = rutaBd
        self.conexion = None
        self.cursor = None
        self.conectaBD()

    def conectaBD(self):
        """Conecta a la base de datos SQLite si no existe una conexión compartida."""
        try:
            if ConexionBD._conexion_compartida is None:
                ConexionBD._conexion_compartida = sqlite3.connect(self.rutaBd)
                print("Conexión de base de datos realizada")
            self.conexion = ConexionBD._conexion_compartida
            self.cursor = self.conexion.cursor()
        except sqlite3.Error as e:
            print(f"Error al conectar a la base de datos: {e}")

    def crear_tabla(self):
        """Crea la tabla 'pokemon' si no existe."""
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS pokemon (
                    name TEXT PRIMARY KEY,
                    type TEXT NOT NULL,
                    hp INTEGER NOT NULL,
                    attack INTEGER NOT NULL,
                    defense INTEGER NOT NULL,
                    spattack INTEGER NOT NULL,
                    spdefense INTEGER NOT NULL,
                    speed INTEGER NOT NULL
                )
            """)
            self.conexion.commit()
            print("Tabla 'pokemon' creada correctamente")
        except sqlite3.Error as e:
            print(f"Error al crear la tabla: {e}")

    def consultaSenParametros(self, consultaSQL):
        """Realiza una consulta sin parámetros."""
        try:
            self.cursor.execute(consultaSQL)
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error en la consulta: {e}")
            return None

    def consultaConParametros(self, consultaSQL, parametros=()):
        """Realiza una consulta con parámetros."""
        try:
            self.cursor.execute(consultaSQL, parametros)
            self.conexion.commit()
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error en la consulta con parámetros: {e}")
            return None

    def pechaBD(self):
        """Cierra la conexión con la base de datos. Solo cierra si es la última conexión activa."""
        try:
            if self.cursor:
                self.cursor.close()
            if self.conexion:
                self.conexion.close()
                ConexionBD._conexion_compartida = None  # Liberar la conexión compartida
                print("Conexión cerrada correctamente.")
        except sqlite3.Error as e:
            print(f"Error al cerrar la conexión: {e}")

    # Métodos para operar en la base de datos
    def insertar_pokemon_uno(self, datos):
        try:
            self.cursor.execute(
                "INSERT INTO pokemon (name, type, hp, attack, defense, spattack, spdefense, speed) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                datos,
            )
            self.conexion.commit()
            print("Pokémon insertado correctamente.")
        except sqlite3.Error as e:
            print(f"Error al insertar el Pokémon: {e}")

    def insertar_pokemon_muchos(self, datos):
        try:
            self.cursor.executemany(
                "INSERT INTO pokemon (name, type, hp, attack, defense, spattack, spdefense, speed) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                datos,
            )
            self.conexion.commit()
            print("Pokémones insertados correctamente.")
        except sqlite3.Error as e:
            print(f"Error al insertar los Pokémones: {e}")

    def update_pokemons(self, hp, clave):
        try:
            self.cursor.execute(
                "UPDATE pokemon SET hp = ? WHERE name = ?",
                (hp, clave),
            )
            self.conexion.commit()
            print("Vida del Pokémon actualizada con éxito.")
        except sqlite3.Error as e:
            print(f"Error al actualizar la vida del Pokémon: {e}")

    def delete_pokemon(self, clave):
        try:
            self.cursor.execute(
                "DELETE FROM pokemon WHERE name = ?", (clave,)
            )
            if self.cursor.rowcount == 0:
                print("No se encontró ningún Pokémon con ese nombre.")
            else:
                self.conexion.commit()
                print("Pokémon borrado con éxito.")
        except sqlite3.Error as e:
            print(f"Error al borrar el Pokémon de la tabla: {e}")

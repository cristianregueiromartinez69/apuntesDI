from PyQt6.QtCore import Qt, QAbstractListModel  # Importa clases necesarias para crear un modelo de datos.
from PyQt6.QtGui import QImage  # Importa la clase QImage para manejar imágenes.

# Carga las imágenes que se usarán para representar el estado de las tareas.
tick = QImage("C:/Users/crm23/OneDrive/Escritorio/dam2Clase/Desarrollo de Interfaces/apuntesExamen/apuntesExamenDI/tick.png")  # Imagen para tareas completadas.
noHecha = QImage("C:/Users/crm23/OneDrive/Escritorio/dam2Clase/Desarrollo de Interfaces/apuntesExamen/apuntesExamenDI/noHecha.png")  # Imagen para tareas no completadas.


# Definición de la clase ModeloTareas, que hereda de QAbstractListModel.
class ModeloTareas(QAbstractListModel):
    def __init__(self, tarefas=None):
        """
        Constructor de la clase.
        - `tarefas`: lista de tuplas que representan las tareas (por defecto, una lista vacía).
        """
        super().__init__()
        self.tarefas = tarefas or []  # Si no se proporciona una lista, se inicializa con una lista vacía.

    def data(self, index, role):
        """
        Devuelve los datos de un elemento según su rol.
        - `index`: índice del elemento en el modelo.
        - `role`: tipo de datos que se solicita (texto, decoración, etc.).
        """
        if role == Qt.ItemDataRole.DisplayRole:  # Rol para mostrar texto en la lista.
            _, texto = self.tarefas[index.row()]  # Obtiene el texto de la tarea.
            return texto  # Devuelve el texto de la tarea.

        if role == Qt.ItemDataRole.DecorationRole:  # Rol para mostrar imágenes o iconos.
            estado, _ = self.tarefas[index.row()]  # Obtiene el estado (True o False) de la tarea.
            if estado:
                return tick  # Si la tarea está completada, devuelve la imagen de "tick".
            else:
                return noHecha  # Si la tarea no está completada, devuelve la imagen de "noHecha".

    def rowCount(self, index):
        """
        Devuelve el número de filas en el modelo.
        - `index`: índice del modelo (no se usa en este caso).
        """
        return len(self.tarefas)  # Retorna la cantidad de tareas en la lista.

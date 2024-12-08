from PyQt6.QtCore import QAbstractTableModel, Qt
from PyQt6 import QtGui


class ModeloTabla(QAbstractTableModel):
    def __init__(self, tabla=None):
        super().__init__()
        self.tabla = tabla or []
        self.columnas = ["Name", "Type", "HP", "Attack", "Defense", "Sp.Attack", "Sp.Defense", "Speed"]


    def rowCount(self, indice):
        return len(self.tabla)

    def columnCount(self, indice):
        return len(self.tabla[0]) if len(self.tabla) != 0 else 0

    def data(self, indice, rol):
        if rol == Qt.ItemDataRole.EditRole or rol == Qt.ItemDataRole.DisplayRole:
            valor = self.tabla[indice.row()][indice.column()]
            return valor

        if rol == Qt.ItemDataRole.BackgroundRole:
            if self.tabla[indice.row()][1] == "Electric":
                return QtGui.QColor("yellow")
            elif self.tabla[indice.row()][1] == "Fire":
                return QtGui.QColor("red")
            elif self.tabla[indice.row()][1] == "Grass/Poison":
                return QtGui.QColor("green")
            elif self.tabla[indice.row()][1] == "Water":
                return QtGui.QColor("blue")
            elif self.tabla[indice.row()][1] == "Normal/Fairy":
                return QtGui.QColor("white")
            elif self.tabla[indice.row()][1] == "Ghost/Poison":
                return QtGui.QColor("magenta")
            elif self.tabla[indice.row()][1] == "Rock/Ground":
                return QtGui.QColor("gray")
            elif self.tabla[indice.row()][1] == "Psychic":
                return QtGui.QColor("pink")
            elif self.tabla[indice.row()][1] == "Normal":
                return QtGui.QColor("white")
            elif self.tabla[indice.row()][1] == "Dragon/Flying":
                return QtGui.QColor("orange")



    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Horizontal:
            return self.columnas[section]
        return None

    def flags(self, index):
        if index.column() == 1:
            return Qt.ItemFlag.ItemIsEnabled
        return Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable

    '''

        if rol == Qt.ItemDataRole.BackgroundRole:
            if self.tabla[indice.row()][2] == "Hombre":
                return QtGui.QColor("cyan")
            elif self.tabla[indice.row()][2] == "Mujer":
                return QtGui.QColor("pink")
            elif self.tabla[indice.row()][2] == "Otro":
                return QtGui.QColor("orange")

        if rol == Qt.ItemDataRole.ForegroundRole:
            if self.tabla[indice.row()][3]:
                 if indice.column() == 3:
                     return QtGui.QColor("red")

        if rol == Qt.ItemDataRole.DecorationRole:
            if isinstance(self.tabla[indice.row()][indice.column()], bool):
                if self.tabla[indice.row()][indice.column()]:
                    return QtGui.QIcon("tick.png")

    def flags(self, index):
        if index.column() == 1:
            return Qt.ItemFlag.ItemIsEnabled
        return Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsEditable | Qt.ItemFlag.ItemIsSelectable



'''
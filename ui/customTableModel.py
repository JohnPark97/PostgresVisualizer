
from PyQt6.QtCore import Qt, QAbstractTableModel, QModelIndex
from services.queryService import *

# NOT IN USE
class CustomTableModel(QAbstractTableModel):
    def __init__(self, data, headers):
        super(CustomTableModel, self).__init__()
        self._data = data
        self.headerLabels = headers

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])

    def headerData(self, section, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return self.headerLabels[section]
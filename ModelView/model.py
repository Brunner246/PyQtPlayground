from PyQt5.QtCore import QAbstractListModel, QModelIndex, Qt
from PyQt5.QtGui import QIcon


class ListModel(QAbstractListModel):
    def __init__(self, data=None, parent=None):
        QAbstractListModel.__init__(self, parent)
        self._data = data or []
        self._icons = [QIcon('ModelView/edit_icon_disabled.svg') for _ in self._data]
        self._previous_index: QModelIndex = None

    def rowCount(self, parent=None):
        return len(self._data)

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return self._data[index.row()]
        elif role == Qt.DecorationRole:
            return self._icons[index.row()]

    def setData(self, index, value, role=Qt.EditRole):
        if role == Qt.DecorationRole:
            self._icons[index.row()] = value
            self.dataChanged.emit(index, index, [role])
            print(f"Set data at row {index.row()} to {value}")
            return True
        return False

    def flags(self, index):
        return super().flags(index) | Qt.ItemIsSelectable | Qt.ItemIsEditable

    def item_clicked(self, index: QModelIndex):
        print(f'Item clicked: {index.data()}')
        self.setData(index, QIcon('ModelView/edit_icon_enabled.svg'), Qt.DecorationRole)
        if self._previous_index is not None and self._previous_index != index:
            self.setData(self._previous_index, QIcon('ModelView/edit_icon_disabled.svg'), Qt.DecorationRole)
        self._previous_index = index

from PyQt5.QtCore import QAbstractListModel, QModelIndex, Qt
from PyQt5.QtGui import QIcon


class ListModel(QAbstractListModel):
    def __init__(self, data=None, parent=None):
        QAbstractListModel.__init__(self, parent)
        self._data = data or []
        self._icon_states = [QIcon.Off for _ in self._data]
        self._previous_index: QModelIndex = None
        self._icon = QIcon()
        self._icon.addFile("ModelView/resources/edit_icon_disabled.svg", mode=QIcon.Normal, state=QIcon.Off)
        self._icon.addFile("ModelView/resources/edit_icon_enabled.svg", mode=QIcon.Normal, state=QIcon.On)

    def rowCount(self, parent=None):
        return len(self._data)

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return self._data[index.row()]
        elif role == Qt.DecorationRole:
            return self._icon
        elif role == Qt.UserRole:
            return self._icon_states[index.row()]

    def setData(self, index, value, role=Qt.EditRole):
        if role == Qt.DecorationRole:
            self.dataChanged.emit(index, index, [role])
            return True
        elif role == Qt.UserRole:
            self._icon_states[index.row()] = value
            return True
        return False

    def flags(self, index):
        return super().flags(index) | Qt.ItemIsSelectable | Qt.ItemIsEditable

    def connect_delegate(self, delegate):
        delegate.iconClicked.connect(lambda: print(f"hello from delegate"))
        delegate.iconClicked.connect(self.item_clicked)

    def item_clicked(self, index: QModelIndex):
        if self.data(index, Qt.UserRole) == QIcon.Off:
            self.setData(index, QIcon.On, Qt.UserRole)
        else:
            self.setData(index, QIcon.Off, Qt.UserRole)
        if self._previous_index is not None and self._previous_index != index:
            self.setData(self._previous_index, QIcon.Off, Qt.UserRole)
        self._previous_index = index
        self.dataChanged.emit(index, index, [Qt.DecorationRole])

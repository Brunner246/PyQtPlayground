from PyQt5.QtCore import QAbstractListModel, QModelIndex, Qt
from PyQt5.QtGui import QIcon

from ModelView.delegate import ButtonState


class ListModel(QAbstractListModel):
    def __init__(self, data=None, parent=None):
        QAbstractListModel.__init__(self, parent)
        self._data = data or []
        self._icons = [QIcon('ModelView/edit_icon_disabled.svg') for _ in self._data]
        self._icon_states = [ButtonState.disabled for _ in self._data]
        self._previous_index: QModelIndex = None

    def rowCount(self, parent=None):
        return len(self._data)

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return self._data[index.row()]
        elif role == Qt.DecorationRole:
            return self._icons[index.row()]
        elif role == Qt.UserRole:
            return self._icon_states[index.row()]

    def setData(self, index, value, role=Qt.EditRole):
        if role == Qt.DecorationRole:
            self._icons[index.row()] = value
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
        if self.data(index, Qt.UserRole) == ButtonState.disabled:
            self.setData(index, QIcon('ModelView/edit_icon_enabled.svg'), Qt.DecorationRole)
            self.setData(index, ButtonState.enabled, Qt.UserRole)
        else:
            self.setData(index, QIcon('ModelView/edit_icon_disabled.svg'), Qt.DecorationRole)
            self.setData(index, ButtonState.disabled, Qt.UserRole)
        if self._previous_index is not None and self._previous_index != index:
            self.setData(self._previous_index, QIcon('ModelView/edit_icon_disabled.svg'), Qt.DecorationRole)
            self.setData(self._previous_index, ButtonState.disabled, Qt.UserRole)
        self._previous_index = index
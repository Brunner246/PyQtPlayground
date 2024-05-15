from enum import IntEnum

from PyQt5.QtCore import QEvent, QRect, Qt, pyqtSignal, QModelIndex
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QStyledItemDelegate, QStyle, QApplication


class ButtonState(IntEnum):
    enabled = 1
    disabled = 2


class IconButtonDelegate(QStyledItemDelegate):
    iconClicked = pyqtSignal(QModelIndex)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.icon_state = ButtonState.disabled
        self.icon = QIcon("ModelView/edit_icon_disabled.svg")
        # self.icon.addFile("ModelView/edit_icon_enabled.svg", mode=QIcon.Normal, state=QIcon.On)

    def paint(self, painter, option, index):
        # image = index.model().data(index, Qt.DecorationRole)
        QApplication.style().drawControl(QStyle.CE_ItemViewItem, option, painter)
        icon_state = index.data(Qt.UserRole)
        if icon_state == ButtonState.enabled:
            self.icon = QIcon("ModelView/edit_icon_enabled.svg")
        else:
            self.icon = QIcon("ModelView/edit_icon_disabled.svg")

        icon_rect = QRect(option.rect.right() - 30, option.rect.top(), 30, option.rect.height())
        self.icon.paint(painter, icon_rect)

        text_rect = QRect(option.rect.left(), option.rect.top(), option.rect.width() - 30, option.rect.height())
        text = index.data()
        painter.drawText(text_rect, Qt.AlignVCenter, text)

    def editorEvent(self, event, model, option, index):
        if event.type() == QEvent.MouseButtonRelease:
            if QRect(option.rect.right() - 30, option.rect.top(), 30, option.rect.height()).contains(event.pos()):
                icon_state = index.data(Qt.UserRole)
                if icon_state == ButtonState.disabled:
                    model.setData(index, ButtonState.enabled, Qt.UserRole)
                else:
                    model.setData(index, ButtonState.disabled, Qt.UserRole)
                self.iconClicked.emit(index)
        return True

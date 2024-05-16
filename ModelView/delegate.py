from PyQt5.QtCore import QEvent, QRect, Qt, pyqtSignal, QModelIndex
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QStyledItemDelegate, QStyle, QApplication


class IconButtonDelegate(QStyledItemDelegate):
    iconClicked = pyqtSignal(QModelIndex)
    textClicked = pyqtSignal(QModelIndex)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.icon = QIcon()
        self.icon.addFile("ModelView/resources/edit_icon_disabled.svg", mode=QIcon.Normal, state=QIcon.Off)
        self.icon.addFile("ModelView/resources/edit_icon_enabled.svg", mode=QIcon.Normal, state=QIcon.On)
        self.icon_state = QIcon.Off

    def paint(self, painter, option, index):
        QApplication.style().drawControl(QStyle.CE_ItemViewItem, option, painter)

        icon_state = index.data(Qt.UserRole)
        if icon_state == QIcon.On:
            pixmap = self.icon.pixmap(24, 24, QIcon.Normal, QIcon.On)
        else:
            pixmap = self.icon.pixmap(24, 24, QIcon.Normal, QIcon.Off)

        icon_rect = QRect(option.rect.right() - 24, option.rect.top(), 24, option.rect.height())
        painter.drawPixmap(icon_rect, pixmap)

        text_rect = QRect(option.rect.left(), option.rect.top(), option.rect.width() - 24, option.rect.height())
        text = index.data()
        painter.drawText(text_rect, Qt.AlignVCenter, text)

    def editorEvent(self, event, model, option, index):
        if event.type() == QEvent.MouseButtonRelease:
            if QRect(option.rect.right() - 24, option.rect.top(), 24, option.rect.height()).contains(event.pos()):
                self.icon_clicked(index, model)
            elif QRect(option.rect.left(), option.rect.top(), option.rect.width() - 24, option.rect.height()).contains(event.pos()):
                self.text_clicked(index)
        return True

    def text_clicked(self, index):
        self.textClicked.emit(index)

    def icon_clicked(self, index, model):
        icon_state = index.data(Qt.UserRole)
        if icon_state == QIcon.Off:
            model.setData(index, QIcon.On, Qt.UserRole)
        else:
            model.setData(index, QIcon.Off, Qt.UserRole)
        self.iconClicked.emit(index)

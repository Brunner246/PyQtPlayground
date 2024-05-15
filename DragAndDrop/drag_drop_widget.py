import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QFrame)
from PyQt5.QtGui import QDrag
from PyQt5.QtCore import Qt, QMimeData


class DraggableButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.drag_start_position = None
        self.setText(text)

    # override
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()

    # override
    def mouseMoveEvent(self, event):
        drag = QDrag(self)
        mime_data = QMimeData()
        drag.setMimeData(mime_data)
        drag.exec_(Qt.MoveAction)


class DropTargetWidget(QFrame):

    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
        self.setObjectName("Containers")

        self.container_v_box = QVBoxLayout()
        self.container_v_box.setAlignment(Qt.AlignTop)
        self.setLayout(self.container_v_box)

    def add_button(self, button):
        self.container_v_box.addWidget(button, 0, Qt.AlignCenter)

    # override
    def dragEnterEvent(self, event):
        event.acceptProposedAction()

    # override
    def dropEvent(self, event):
        event.setDropAction(Qt.MoveAction)
        source = event.source()

        if source not in self.children():
            event.setAccepted(True)
            self.container_v_box.addWidget(source, 0, Qt.AlignCenter)
        else:
            event.setAccepted(False)


class DragDropWidgetsEx(QWidget):

    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        self.setMinimumSize(500, 500)
        self.setWindowTitle("Drag and Drop Widgets Example")
        self.setup_widgets()
        self.show()

    def setup_widgets(self):
        left_target = DropTargetWidget()
        label_a = DraggableButton("A")
        left_target.add_button(label_a)
        label_b = DraggableButton("B")
        left_target.add_button(label_b)

        right_target = DropTargetWidget()
        label_c = DraggableButton("C")
        right_target.add_button(label_c)
        label_d = DraggableButton("D")
        right_target.add_button(label_d)

        main_h_box = QHBoxLayout()
        main_h_box.addWidget(left_target)
        main_h_box.addWidget(right_target)

        self.setLayout(main_h_box)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     with open("style.css", "r") as f:
#         style_sheet = f.read()
#     app.setStyleSheet(style_sheet)
#     window = DragDropWidgetsEx()
#     sys.exit(app.exec_())

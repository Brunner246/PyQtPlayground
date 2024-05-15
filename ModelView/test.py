from PyQt5.QtWidgets import QApplication, QListView, QStyledItemDelegate, QVBoxLayout, QWidget, QLabel, QHBoxLayout, QStyle, QPushButton
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QIcon, QPixmap, QPainter
from PyQt5.QtCore import Qt, QEvent, QRect

#
#
# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.listView = QListView()
#         self.listView.setItemDelegate(IconButtonDelegate())
#
#         # Set the spacing between items
#         self.listView.setSpacing(10)  # adjust this value as needed
#
#         # Create a model and add items to it
#         model = QStandardItemModel()
#         for i in range(10):
#             item = QStandardItem(f"Item {i}")
#             model.appendRow(item)
#
#         # Set the model on the view
#         self.listView.setModel(model)
#
#         layout = QVBoxLayout()
#         self.setLayout(layout)
#         layout.addWidget(self.listView)
#
# def main():
#     app = QApplication([])
#
#     window = MainWindow()
#     window.show()
#
#     app.exec_()
#
# if __name__ == '__main__':
#     main()
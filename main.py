from PyQt5.QtWidgets import QApplication

from ModelView.model import ListModel
from ModelView.view import ExampleView

if __name__ == '__main__':
    app = QApplication(list())

    list_data = [f'building plan {i}' for i in range(10)]

    model = ListModel(list_data)
    view = ExampleView(model)
    app.exec_()

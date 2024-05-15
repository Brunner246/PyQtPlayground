from PyQt5.QtCore import QAbstractListModel, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QListView, QMainWindow, QSplitter

from ModelView.delegate import IconButtonDelegate


class ExampleView(QMainWindow):
    def __init__(self, model: QAbstractListModel):
        super().__init__()
        self.view = QListView(self)
        self.view.setItemDelegate(IconButtonDelegate())
        self.model = model
        self.view.setModel(self.model)

        self.web_view = QWebEngineView()
        self.web_view.load(QUrl("https://incon.ai/"))

        splitter = QSplitter(self)
        splitter.addWidget(self.view)
        splitter.addWidget(self.web_view)

        self.setCentralWidget(splitter)

        self.init_ui()
        self.signal_slot_connections()

    def init_ui(self):
        self.setGeometry(100, 100, 1_000, 800)
        self.setWindowTitle('Simple List Model Example')
        self.show()

    def signal_slot_connections(self):
        self.view.clicked.connect(self.model.item_clicked)
        self.web_view.loadFinished.connect(lambda result: print(f'Web view loaded: {result}'))
        self.model.connect_delegate(self.view.itemDelegate())

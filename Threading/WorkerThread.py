import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
from PyQt5.QtCore import QThread, pyqtSignal


class Worker(QThread):
    progress = pyqtSignal(int)

    def run(self):
        for i in range(101):
            self.msleep(100)
            if i % 10 == 0:
                print(f'Progress: {i}%')
            self.progress.emit(i)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('PyQt Threading')
        self.setGeometry(100, 100, 300, 200)

        self.label = QLabel('Progress: 0%', self)
        self.button = QPushButton('Start Task', self)
        self.button.clicked.connect(self.start_task)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.worker = Worker()
        self.worker.progress.connect(self.update_progress)

    def start_task(self):
        self.worker.start()

    def update_progress(self, value):
        self.label.setText(f'Progress: {value}%')
        if value == 100:
            self.button.setEnabled(True)
        else:
            self.button.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton
)

class CounterView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Counter App")
        self.layout = QVBoxLayout()

        self.label = QLabel("0")
        self.btn_increment = QPushButton("+")
        self.btn_decrement = QPushButton("-")
        self.btn_reset = QPushButton("Reset")

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.btn_increment)
        self.layout.addWidget(self.btn_decrement)
        self.layout.addWidget(self.btn_reset)
        self.setLayout(self.layout)


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     controller = CounterController()
#     controller.view.show()
#     sys.exit(app.exec())
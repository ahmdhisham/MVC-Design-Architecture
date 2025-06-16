import sys
from PyQt6.QtWidgets import QApplication, QLabel
from ..models.counter import Counter

app = QApplication(sys.argv)
label = QLabel("Hello World!")
label.show()

if __name__ == "__main__":
    app.exec()
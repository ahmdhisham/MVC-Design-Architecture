import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout ,QLabel, QPushButton
)

class CounterView(QWidget):

    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
            background-color: #00FFA0; 
            color: orange;
            """) 
        self.setWindowTitle("Counter App")
        self.setFixedSize(400, 200)
        self.layout = QVBoxLayout()
        # self.layout = QHBoxLayout

        self.label = QLabel("0")
        self.label.setStyleSheet("background-color: lightpurple; padding: 5px; font-size: 24px;")
        self.btn_increment = QPushButton("+")
        self.btn_increment.setStyleSheet("""
                        color: gray;
                        background-color: yellow;
                        selection-color: blue;
                        """)
        self.btn_decrement = QPushButton("-")
        self.btn_reset = QPushButton("Reset")

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.btn_increment)
        self.layout.addWidget(self.btn_decrement)
        self.layout.addWidget(self.btn_reset)
        self.setLayout(self.layout)

import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout ,QLabel, QPushButton
)

class CounterView(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Counter App")
        self.setFixedSize(400, 180)
        self.layout = QVBoxLayout()
        self.setStyleSheet("""
                        background-color: #00FF90; 
                        """) 

        self.label = QLabel("0")
        self.label.setStyleSheet("""
                        
                        qproperty-alignment: 'AlignCenter';
                        background-color: #182c25;
                        border-radius: 5px;   /* Corner radius */ 
                        font-size: 21px; 
                        color: white;
                        
                        """)

        self.btn_increment = QPushButton("+")
        self.btn_increment.setStyleSheet("""
                        color: green;
                        background-color: #222222;
                        selection-background-color: blue;
                        """)

        self.btn_decrement = QPushButton("-")
        self.btn_decrement.setStyleSheet("""
                        color: red;
                        background-color: #222222;
                        selection-background-color: blue;
                        """)

        self.btn_reset = QPushButton("Reset")
        self.btn_reset.setStyleSheet("""
                        color: orange;
                        background-color: #222222;
                        selection-background-color: blue;
                        """)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.btn_increment)
        self.layout.addWidget(self.btn_decrement)
        self.layout.addWidget(self.btn_reset)
        self.setLayout(self.layout)
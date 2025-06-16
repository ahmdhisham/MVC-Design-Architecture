import sys
from PySide6.QtWidgets import QApplication
from controller.counter_ctrl import CounterController

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = CounterController()
    controller.view.show()
    sys.exit(app.exec())
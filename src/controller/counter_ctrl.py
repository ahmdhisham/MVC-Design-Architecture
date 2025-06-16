from ..model.counter import Counter
from ..view.counterUI import CounterView

class CounterController:
    def __init__(self):
        self.model = Counter()
        self.view = CounterView()

        # Connect buttons to model methods
        self.view.btn_increment.clicked.connect(self.increment)
        self.view.btn_decrement.clicked.connect(self.decrement)
        self.view.btn_reset.clicked.connect(self.reset)

        # Update the view initially
        self.update_view()

    def increment(self):
        self.model.increment()
        self.update_view()

    def decrement(self):
        self.model.decrement()
        self.update_view()

    def reset(self):
        self.model.reset()
        self.update_view()

    def update_view(self):
        self.view.label.setText(str(self.model.value))
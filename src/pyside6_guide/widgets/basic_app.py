"""
basic_app.py
by HundredVisionsGuy
A demo of the most basic input/output: labels, text inputs, and buttons.
"""

import sys
from PySide6.QtWidgets import (
    QApplication,
    QSpinBox,
    QDoubleSpinBox,
    QComboBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Basic App")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(320, 240)

        layout = QVBoxLayout()
        title_label = QLabel("Basic App: a simple greeting app.")

        # TODO: add a text input for user's name
        self.name_input = QLineEdit(placeholderText="Name")

        # TODO: add one or more horizontal layouts with widgets side by side
        age_layout = QHBoxLayout()
        age_label = QLabel("Age: ")
        self.age_spinbox = QSpinBox()
        self.age_spinbox.setValue(5)
        self.age_spinbox.setMinimum(1)
        self.age_spinbox.setMaximum(125)
        self.age_spinbox.setSingleStep(5)
        age_layout.addWidget(age_label)
        age_layout.addWidget(self.age_spinbox)

        money_layout = QHBoxLayout()
        money_label = QLabel("Total price: ")
        self.money_spinbox = QDoubleSpinBox()
        self.money_spinbox.setPrefix("$")
        money_layout.addWidget(money_label)
        money_layout.addWidget(self.money_spinbox)

        # TODO: add a push button to greet user
        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.get_input)

        # TODO: add a label to greet user
        self.instructions = "Enter your name, then click the button."
        self.output_label = QLabel(self.instructions)
        self.output_label.setWordWrap(True)

        """
        Challenges:
            * Add another text input (last name, home town, etc.)
            * Add a clear button that, when clicked will
                - clear the text in the name input
                - reset the output text to its initial value
        """

        # add widgets & layouts to main layout
        layout.addWidget(title_label)
        layout.addWidget(self.name_input)
        layout.addLayout(age_layout)
        layout.addLayout(money_layout)
        layout.addWidget(submit_button)
        layout.addWidget(self.output_label)

        # [OPTIONAL] Add a stretch to move everything up
        layout.addStretch()

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)

    def get_input(self):
        """grab input, process input, display output"""
        output = ""
        name = self.name_input.text()
        age = self.age_spinbox.value()
        money_string = self.money_spinbox.text()
        money = self.money_spinbox.value()
        if not name:
            output = "WARNING: you did not enter your name. Please enter "
            output += "your name."
        else:
            output = f"You entered {name} as your name and {age} as age."
        self.output_label.setText(output)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()
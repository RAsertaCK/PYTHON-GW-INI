import sys
import math
from abc import ABC, abstractmethod
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox

class Ops(ABC):
    @abstractmethod
    def calculate(self, num1, num2):
        pass

class Tambah(Ops):
    def calculate(self, num1, num2):
        return num1 + num2

class Kurang(Ops):
    def calculate(self, num1, num2):
        return num1 - num2

class Kali(Ops):
    def calculate(self, num1, num2):
        return num1 * num2

class Bagi(Ops):
    def calculate(self, num1, num2):
        return num1 / num2 if num2 != 0 else "Error (Divide by Zero)"

class Pangkat(Ops):
    def calculate(self, num1, num2):
        return num1 ** num2

class Log(Ops):
    def calculate(self, num1, num2):
        return math.log(num1, num2) if num1 > 0 and num2 > 0 else "Error (Invalid Log)"

class Kalkulator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __add__(self):
        return Tambah().calculate(self.num1, self.num2)

    def __sub__(self):
        return Kurang().calculate(self.num1, self.num2)

    def __mul__(self):
        return Kali().calculate(self.num1, self.num2)

    def __truediv__(self):
        return Bagi().calculate(self.num1, self.num2)

    def __pow__(self):
        return Pangkat().calculate(self.num1, self.num2)

    def log(self):
        return Log().calculate(self.num1, self.num2)

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Kalkulator PyQt dengan OOP")
        self.setGeometry(100, 100, 300, 400)

        layout = QVBoxLayout()

        self.label1 = QLabel("Angka 1:")
        self.input1 = QLineEdit()
        layout.addWidget(self.label1)
        layout.addWidget(self.input1)

        self.label_op = QLabel("Operasi:")
        self.op_box = QComboBox()
        self.op_box.addItems(["+", "-", "*", "/", "^", "log"])
        layout.addWidget(self.label_op)
        layout.addWidget(self.op_box)

        self.label2 = QLabel("Angka 2:")
        self.input2 = QLineEdit()
        layout.addWidget(self.label2)
        layout.addWidget(self.input2)

        self.calculate_button = QPushButton("Hitung")
        self.calculate_button.clicked.connect(self.calculate)
        layout.addWidget(self.calculate_button)

        self.result_label = QLabel("Hasil: ")
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def calculate(self):
        try:
            num1 = float(self.input1.text())
            num2 = float(self.input2.text())
            operation = self.operation_box.currentText()

            calc = Kalkulator(num1, num2)

            if operation == "+":
                result = calc.__add__()
            elif operation == "-":
                result = calc.__sub__()
            elif operation == "*":
                result = calc.__mul__()
            elif operation == "/":
                result = calc.__truediv__()
            elif operation == "^":
                result = calc.__pow__()
            elif operation == "log":
                result = calc.log()
            else:
                result = "Error: Operasi tidak dikenal!"

            self.result_label.setText(f"Hasil: {result}")

        except ValueError:
            self.result_label.setText("Error: Input tidak valid!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = App()
    calculator.show()
    sys.exit(app.exec())

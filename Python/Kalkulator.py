import sys
import math
from abc import ABC, abstractmethod
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox

# Abstract Base Class untuk operasi
class Operation(ABC):
    @abstractmethod
    def calculate(self, num1, num2):
        pass

# Subclass untuk setiap operasi
class Addition(Operation):
    def calculate(self, num1, num2):
        return num1 + num2

class Subtraction(Operation):
    def calculate(self, num1, num2):
        return num1 - num2

class Multiplication(Operation):
    def calculate(self, num1, num2):
        return num1 * num2

class Division(Operation):
    def calculate(self, num1, num2):
        return num1 / num2 if num2 != 0 else "Error (Divide by Zero)"

class Exponentiation(Operation):
    def calculate(self, num1, num2):
        return num1 ** num2

class Logarithm(Operation):
    def calculate(self, num1, num2):
        return math.log(num1, num2) if num1 > 0 and num2 > 0 else "Error (Invalid Log)"

# Class Calculator yang memanfaatkan dunder methods
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __add__(self):
        return Addition().calculate(self.num1, self.num2)

    def __sub__(self):
        return Subtraction().calculate(self.num1, self.num2)

    def __mul__(self):
        return Multiplication().calculate(self.num1, self.num2)

    def __truediv__(self):
        return Division().calculate(self.num1, self.num2)

    def __pow__(self):
        return Exponentiation().calculate(self.num1, self.num2)

    def log(self):
        return Logarithm().calculate(self.num1, self.num2)

# GUI PyQt
class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Kalkulator PyQt dengan OOP")
        self.setGeometry(100, 100, 300, 400)

        layout = QVBoxLayout()

        # Input angka pertama
        self.label1 = QLabel("Angka 1:")
        self.input1 = QLineEdit()
        layout.addWidget(self.label1)
        layout.addWidget(self.input1)

        # Dropdown operasi
        self.label_op = QLabel("Operasi:")
        self.operation_box = QComboBox()
        self.operation_box.addItems(["+", "-", "*", "/", "^", "log"])
        layout.addWidget(self.label_op)
        layout.addWidget(self.operation_box)

        # Input angka kedua
        self.label2 = QLabel("Angka 2:")
        self.input2 = QLineEdit()
        layout.addWidget(self.label2)
        layout.addWidget(self.input2)

        # Tombol hitung
        self.calculate_button = QPushButton("Hitung")
        self.calculate_button.clicked.connect(self.calculate)
        layout.addWidget(self.calculate_button)

        # Label hasil
        self.result_label = QLabel("Hasil: ")
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def calculate(self):
        try:
            num1 = float(self.input1.text())
            num2 = float(self.input2.text())
            operation = self.operation_box.currentText()

            calc = Calculator(num1, num2)

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

# Main Program
if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = CalculatorApp()
    calculator.show()
    sys.exit(app.exec())

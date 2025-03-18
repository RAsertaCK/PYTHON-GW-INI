import sys
import math
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QGridLayout, QLabel, QPushButton
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt, QPropertyAnimation, QRect

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Kalkulator PyQt Advanced")
        self.setGeometry(100, 100, 400, 500)
        
        # Layout utama
        main_layout = QVBoxLayout()
        font = QFont("Arial", 14)

        # Display hasil
        self.display = QLabel("0")
        self.display.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        self.display.setStyleSheet("background-color: #3a3f4b; color: white; padding: 10px; border-radius: 5px;")
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        main_layout.addWidget(self.display)

        # Layout tombol
        grid_layout = QGridLayout()

        # Tombol angka, operasi, backspace, dan trigonometrinya
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('sin', 1, 4),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('cos', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('tan', 3, 4),
            ('0', 4, 0), ('.', 4, 1), ('^', 4, 2), ('+', 4, 3), ('⌫', 4, 4),
            ('C', 5, 0), ('log', 5, 1), ('=', 5, 2, 1, 3)
        ]

        # Loop buat bikin tombol-tombolnya
        for btn_info in buttons:
            if len(btn_info) == 3:
                text, row, col = btn_info
                rowspan, colspan = 1, 1
            elif len(btn_info) == 5:
                text, row, col, rowspan, colspan = btn_info

            btn = QPushButton(text)
            btn.setFont(font)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #61afef; 
                    color: white; 
                    padding: 10px; 
                    border-radius: 5px;
                }
                QPushButton:hover {
                    background-color: #528bde;
                }
            """)
            btn.clicked.connect(lambda _, b=text: self.on_button_click(b))
            grid_layout.addWidget(btn, row, col, rowspan, colspan)

            # Animasi tombol pas dipencet
            animation = QPropertyAnimation(btn, b"geometry")
            animation.setDuration(100)
            animation.setStartValue(QRect(btn.x(), btn.y(), btn.width(), btn.height()))
            animation.setEndValue(QRect(btn.x(), btn.y() + 3, btn.width(), btn.height()))
            btn.pressed.connect(animation.start)

        main_layout.addLayout(grid_layout)
        self.setLayout(main_layout)

        # Styling utama
        self.setStyleSheet("""
            QWidget {
                background-color: #282c34;
                color: white;
            }
            QLabel {
                font-size: 18px;
            }
        """)

    def on_button_click(self, button_text):
        current_text = self.display.text()

        if button_text == "=":
            try:
                current_text = current_text.replace("^", "**")

                # Trigonometri
                if "sin" in current_text:
                    result = math.sin(math.radians(float(current_text.replace("sin", ""))))
                elif "cos" in current_text:
                    result = math.cos(math.radians(float(current_text.replace("cos", ""))))
                elif "tan" in current_text:
                    result = math.tan(math.radians(float(current_text.replace("tan", ""))))
                elif "log" in current_text:
                    parts = current_text.split("log")
                    if len(parts) == 2:
                        base = float(parts[0]) if parts[0] else math.e
                        num = float(parts[1])
                        result = math.log(num, base)
                    else:
                        raise ValueError
                else:
                    result = eval(current_text)

                self.display.setText(str(result))
            except:
                self.display.setText("Error")

        elif button_text == "C":
            self.display.setText("0")

        elif button_text == "⌫":
            if current_text != "0" and len(current_text) > 1:
                self.display.setText(current_text[:-1])
            else:
                self.display.setText("0")

        else:
            if current_text == "0" or current_text == "Error":
                self.display.setText(button_text)
            else:
                self.display.setText(current_text + button_text)

# Main Program
if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = CalculatorApp()
    calculator.show()
    sys.exit(app.exec())

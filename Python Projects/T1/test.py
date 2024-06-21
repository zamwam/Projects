import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Simple GUI")
        self.setGeometry(300, 300, 300, 200)

        layout = QVBoxLayout()

        label = QLabel("Enter your name:")
        self.nameEdit = QLineEdit()
        button = QPushButton("Click me!")

        layout.addWidget(label)
        layout.addWidget(self.nameEdit)
        layout.addWidget(button)

        button.clicked.connect(self.onButtonClick)

        self.setLayout(layout)

    def onButtonClick(self):
        name = self.nameEdit.text()
        print(f"Hello, {name}!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
import sys

from PySide6.QtWidgets import (QApplication, QDialog, QLineEdit, QPushButton, QVBoxLayout)


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("dialog")
        self.lineEdit = QLineEdit("输入点什么呢")
        self.button = QPushButton("点击")
        layout = QVBoxLayout()
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.button)
        self.setLayout(layout)
        self.button.clicked.connect(self.test_func)

    def test_func(self):
        print(f"{self.lineEdit.text()}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec())

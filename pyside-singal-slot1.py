import sys
from PySide6.QtWidgets import QApplication, QPushButton, QLineEdit, QHBoxLayout, QMainWindow, QWidget

app = QApplication([])
window = QMainWindow()
window.resize(400,400)
cent = QWidget()
window.setCentralWidget(cent)
qhL = QHBoxLayout()
lineEdit = QLineEdit()
lineEdit.resize(40,40)

button = QPushButton("clear")
button.resize(40,40)
button.clicked.connect(lineEdit.clear)

qhL.addWidget(lineEdit)
qhL.addWidget(button)

cent.setLayout(qhL)
window.show()
sys.exit(app.exec())

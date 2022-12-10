import sys

from PySide6.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem

data = {"Project A": ["file_a.py", "file_a.txt", "something.xls"],
        "Project B": ["file_b.csv", "photo.jpg"],
        "Project C": []}

if __name__ == '__main__':
    app = QApplication()

    tree = QTreeWidget()
    tree.setColumnCount(2)
    tree.setHeaderLabels(["name", "type"])
    items = []
    for key, values in data.items():
        item = QTreeWidgetItem([key])
        for name in values:
            ext = name.split(".")[-1].upper()
            child = QTreeWidgetItem([name, ext])
            item.addChild(child)
        items.append(item)

    tree.insertTopLevelItems(0, items)
    tree.show()

    sys.exit(app.exec())

from PyQt5 import QtWidgets
import sys

BUTTONS = {
    "0": (3, 0),

    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),

    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),

    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),

    ".": (3, 1),
}

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle('Calculator')
        self.setFixedSize(300, 300)
        layout = QtWidgets.QVBoxLayout()
        self.field = QtWidgets.QLineEdit()
        layout.addWidget(self.field)

        grid = QtWidgets.QGridLayout()
        for text, pos in BUTTONS.items():
            btn = QtWidgets.QPushButton(text)
            grid.addWidget(btn, pos [0], pos[1])

        layout.addLayout(grid)

        widget =  QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
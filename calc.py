import sys
from functools import partial
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt


buttons = {
    '0': (3, 0),
    '.': (3, 1),
    '1': (2, 0),
    '2': (2, 1),
    '3': (2, 2),
    '4': (1, 0),
    '5': (1, 1),
    '6': (1, 2),
    '7': (0, 0),
    '8': (0, 1),
    '9': (0, 2),
    '+': (0, 3),
    '-': (1, 3),
    '/': (2, 3),
    '*': (3, 3),
    '=': (0, 4),
    'C': (1, 4),
    '(': (2, 4),
    ')': (3, 4),
}


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__setupUi()

    def __setupUi(self):
        self.setWindowTitle("Calculator")
        layout = QtWidgets.QVBoxLayout()
        grid = QtWidgets.QGridLayout()
        self._view = QtWidgets.QLineEdit()
        self._view.setFixedHeight(40)
        self._view.setAlignment(Qt.AlignRight)
        self._view.setReadOnly(True)

        for text, pos in buttons.items():
            btn = QtWidgets.QPushButton(text)
            btn.setFixedSize(40, 40)
            if text not in ('=', 'C'):
                btn.clicked.connect(partial(self.btnClicked, text))
            else:
                if text == "=":
                    btn.clicked.connect(self.evaluate)
                elif text == "C":
                    btn.clicked.connect(self.clearText)
            grid.addWidget(btn, pos[0], pos[1])

        layout.addWidget(self._view)
        layout.addLayout(grid)
        mainwidget = QtWidgets.QWidget()
        mainwidget.setLayout(layout)
        self.setCentralWidget(mainwidget)

    def btnClicked(self, text: str):
        if self._view.text() == "ERROR":
            self.clearText()
        self._view.setText(self._view.text() + text)

    def evaluate(self):
        try:
            self._view.setText(str(eval(self._view.text())))
        except Exception as e:
            self._view.setText("ERROR")

    def clearText(self):
        self._view.clear()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())

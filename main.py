import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = QWidget()

    layout = QVBoxLayout()
    label = QLabel("Some text")
    label2 = QLabel("Some other text")
    layout.addWidget(label)
    layout.addWidget(label2)
    w.setLayout(layout)

    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())

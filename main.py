import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLCDNumber, QVBoxLayout
from PyQt5.QtGui import QIcon


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        button_roll = QPushButton('Roll', self)
        lcd = QLCDNumber(self)
        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(button_roll)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Dice Rolling Simulator')
        self.setWindowIcon(QIcon('img/dice.png'))

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())

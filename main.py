import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Dice Rolling Simulator')
        self.setWindowIcon(QIcon('img/dice.png'))

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())

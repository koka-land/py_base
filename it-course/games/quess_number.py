import sys
from PyQt6.QtWidgets import (QMainWindow, QApplication,
                             QVBoxLayout, QWidget,
                             QPushButton, QLabel,
                             QLineEdit)
from PyQt6.QtGui import QIcon
import random

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.game()

    def game(self):
        self.setWindowTitle("Guess the Number")
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(400, 400)
        central_widget = QWidget()
        vbox = QVBoxLayout()
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

        qt_rectangle = self.frameGeometry()
        center_point = QApplication.primaryScreen().geometry().center()
        print(center_point)
        qt_rectangle.moveCenter(center_point)
        self.move(qt_rectangle.topLeft())

        self.text = QLabel(self)
        self.text.setText('Я загадал число от 1 до 128.')
        self.text.move(50, 50)
        font = self.text.font()
        font.setPointSize(16)
        self.text.setFont(font)
        self.text.setFixedSize(300, 50)
        self.text.hide()

        self.text2 = QLabel(self)
        self.text2.setText('Попробуй угадай его!')
        self.text2.move(50, 100)
        font = self.text2.font()
        font.setPointSize(14)
        self.text2.setFont(font)
        self.text2.setFixedSize(300, 50)
        self.text2.hide()

        self.text4 = QLabel(self)
        self.text4.move(50, 150)
        font = self.text2.font()
        font.setPointSize(14)
        self.text4.setFont(font)
        self.text4.setFixedSize(300, 50)
        self.text4.hide()

        self.text3 = QLabel(self)
        self.text3.setText('Введи число:')
        self.text3.move(50, 150)
        font = self.text3.font()
        font.setPointSize(14)
        self.text3.setFont(font)
        self.text3.setFixedSize(300, 50)
        self.text3.hide()

        self.start = QPushButton("Начать игру", self)
        self.start.setFixedSize(100, 50)
        self.start.move(150, 150)
        self.start.clicked.connect(self.start_game)

        self.repeat = QPushButton("Повторить", self)
        self.repeat.setFixedSize(100, 50)
        self.repeat.move(150, 250)
        self.repeat.clicked.connect(self.start_game)
        self.repeat.hide()

        self.close = QPushButton("Выход", self)
        self.close.setFixedSize(100, 50)
        self.close.move(150, 300)
        self.close.clicked.connect(self.close_game)
        self.close.hide()

        self.input_num = QLineEdit(self)
        self.input_num.move(180, 160)
        self.input_num.hide()

        self.choise = QPushButton("Угадать", self)
        self.choise.setFixedSize(100, 50)
        self.choise.move(150, 250)
        self.choise.clicked.connect(self.play_game)
        self.choise.hide()

    def start_game(self):
        self.repeat.hide()
        self.text.setText('Я загадал число от 1 до 128.')
        self.text2.setText('Попробуй угадай его!')
        self.start.hide()
        self.choise.show()
        self.text.show()
        self.text2.show()
        self.text3.show()
        self.text4.hide()
        self.input_num.show()
        self.close.hide()
        self.try_g = 0
        self.num = random.randint(1, 128)

    def play_game(self):
        self.try_g += 1
        a = self.input_num.text()
        self.input_num.setText("")
        self.text.setText(f'Вы ввели число: {a} {self.num}')
        if int(a) > self.num:
            self.text2.setText('Оно больше загаданного')
        elif int(a) < self.num:
            self.text2.setText('Оно меньше загаданного')
        else:
            self.text.setText('Вы угадали!!!')
            self.text2.setText(f'Я загадал число {self.num}!!!')
            self.text4.setText(f'Всего за {self.try_g} попытки!!!')
            self.text3.hide()
            self.input_num.hide()
            self.choise.hide()
            self.text4.show()
            self.repeat.show()
            self.close.show()

    def close_game(self):
        self.close()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
import sys
from PyQt6 import QtWidgets

import test1design #подключение шаблона

class TestApp(QtWidgets.QMainWindow, test1design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.print)

    def print(self):
        s = self.label.text()
        self.label.setText(s + 'QQ')

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = TestApp()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
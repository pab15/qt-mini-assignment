import sys
from PySide2.QtUiTools import QUiLoader #allows us to import .ui files
from PySide2.QtWidgets import QApplication, QLineEdit, QPushButton
from PySide2.QtCore import QFile, QObject

class MainWindow(QObject):

    #class constructor
    def __init__(self, ui_file, parent=None):
        super(MainWindow, self).__init__(parent)

        ui_file = QFile(ui_file)
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.window = loader.load(ui_file)
        
        ui_file.close()

        zeroButton = self.window.findChild(QPushButton, 'zeroButton')
        zeroButton.clicked.connect(self.zero_button_clicked)
        oneButton = self.window.findChild(QPushButton, 'oneButton')
        oneButton.clicked.connect(self.one_button_clicked)
        twoButton = self.window.findChild(QPushButton, 'twoButton')
        twoButton.clicked.connect(self.two_button_clicked)
        threeButton = self.window.findChild(QPushButton, 'threeButton')
        threeButton.clicked.connect(self.three_button_clicked)
        fourButton = self.window.findChild(QPushButton, 'fourButton')
        fourButton.clicked.connect(self.four_button_clicked)
        fiveButton = self.window.findChild(QPushButton, 'fiveButton')
        fiveButton.clicked.connect(self.five_button_clicked)
        sixButton = self.window.findChild(QPushButton, 'sixButton')
        sixButton.clicked.connect(self.six_button_clicked)
        sevenButton = self.window.findChild(QPushButton, 'sevenButton')
        sevenButton.clicked.connect(self.seven_button_clicked)
        eightButton = self.window.findChild(QPushButton, 'eightButton')
        eightButton.clicked.connect(self.eight_button_clicked)
        nineButton = self.window.findChild(QPushButton, 'nineButton')
        nineButton.clicked.connect(self.nine_button_clicked)
        addButton = self.window.findChild(QPushButton, 'addButton')
        addButton.clicked.connect(self.add_button_clicked)
        subtractButton = self.window.findChild(QPushButton, 'subtractButton')
        subtractButton.clicked.connect(self.subtract_button_clicked)
        multiplyButton = self.window.findChild(QPushButton, 'multiplyButton')
        multiplyButton.clicked.connect(self.multiply_button_clicked)
        divideButton = self.window.findChild(QPushButton, 'divideButton')
        divideButton.clicked.connect(self.divide_button_clicked)
        equalsButton = self.window.findChild(QPushButton, 'equalsButton')
        equalsButton.clicked.connect(self.equals_button_clicked)
        clearButton = self.window.findChild(QPushButton, 'clearButton')
        clearButton.clicked.connect(self.clear_button_clicked)
        self.window.show()

    def zero_button_clicked(self):
        zeroButton = self.window.findChild(QPushButton, 'zeroButton')
        accumulator = self.window.findChild(QLineEdit, 'accumulatorText')
        currentText = accumulator.text()
        accumulator.setText(currentText + zeroButton.text())
    def one_button_clicked(self):
        oneButton = self.window.findChild(QPushButton, 'oneButton')
        accumulator = self.window.findChild(QLineEdit, 'accumulatorText')
        currentText = accumulator.text()
        accumulator.setText(currentText + oneButton.text())
    def two_button_clicked(self):
        twoButton = self.window.findChild(QPushButton, 'twoButton')
        accumulator = self.window.findChild(QLineEdit, 'accumulatorText')
        currentText = accumulator.text()
        accumulator.setText(currentText + twoButton.text())
    def three_button_clicked(self):
        threeButton = self.window.findChild(QPushButton, 'threeButton')
        accumulator = self.window.findChild(QLineEdit, 'accumulatorText')
        currentText = accumulator.text()
        accumulator.setText(currentText + threeButton.text())
    def four_button_clicked(self):
        fourButton = self.window.findChild(QPushButton, 'fourButton')
        accumulator = self.window.findChild(QLineEdit, 'accumulatorText')
        currentText = accumulator.text()
        accumulator.setText(currentText + fourButton.text())
    def five_button_clicked(self):
        fiveButton = self.window.findChild(QPushButton, 'fiveButton')
        accumulator = self.window.findChild(QLineEdit, 'accumulatorText')
        currentText = accumulator.text()
        accumulator.setText(currentText + fiveButton.text())
    def six_button_clicked(self):
        sixButton = self.window.findChild(QPushButton, 'sixButton')
        accumulator = self.window.findChild(QLineEdit, 'accumulatorText')
        currentText = accumulator.text()
        accumulator.setText(currentText + sixButton.text())
    def seven_button_clicked(self):
        sevenButton = self.window.findChild(QPushButton, 'sevenButton')
        accumulator = self.window.findChild(QLineEdit, 'accumulatorText')
        currentText = accumulator.text()
        accumulator.setText(currentText + sevenButton.text())
    def eight_button_clicked(self):
        eightButton = self.window.findChild(QPushButton, 'eightButton')
        accumulator = self.window.findChild(QLineEdit, 'accumulatorText')
        currentText = accumulator.text()
        accumulator.setText(currentText + eightButton.text())
    def nine_button_clicked(self):
        nineButton = self.window.findChild(QPushButton, 'nineButton')
        accumulator = self.window.findChild(QLineEdit, 'accumulatorText')
        currentText = accumulator.text()
        accumulator.setText(currentText + nineButton.text())
    def add_button_clicked(self):
        addButton = self.window.findChild(QPushButton, 'addButton')
        accumulator = self.window.findChild(QLineEdit, 'accumulatorText')
        currentText = accumulator.text()
        accumulator.setText(currentText + ' ' + addButton.text() + ' ')
    def subtract_button_clicked(self):
        subtractButton = self.window.findChild(QPushButton, 'subtractButton')
        accumulator = self.window.findChild(QLineEdit, 'accumulatorText')
        currentText = accumulator.text()
        accumulator.setText(currentText + ' ' + subtractButton.text() + ' ')
    def multiply_button_clicked(self):
        multiplyButton = self.window.findChild(QPushButton, 'multiplyButton')
        accumulator = self.window.findChild(QLineEdit, 'accumulatorText')
        currentText = accumulator.text()
        accumulator.setText(currentText + ' ' + multiplyButton.text() + ' ')
    def divide_button_clicked(self):
        divideButton = self.window.findChild(QPushButton, 'divideButton')
        accumulator = self.window.findChild(QLineEdit, 'accumulatorText')
        currentText = accumulator.text()
        accumulator.setText(currentText + ' ' + divideButton.text() + ' ')
    def equals_button_clicked(self):
        accumulator = self.window.findChild(QLineEdit, 'accumulatorText')
        inputText = accumulator.text()
        inputText = inputText.split(' ')
        x = 0
        while len(inputText) > 1:
            if (inputText[x] == '*'):
                try:
                    first_num = int(inputText[x - 1])
                    second_num = int(inputText[x + 1])
                except:
                    accumulator.setText('Format Error!')
                else:
                    inputText[x] = first_num * second_num
                    del inputText[x + 1]
                    del inputText[x - 1]
            elif (inputText[x] == '/'):
                try:
                    first_num = int(inputText[x - 1])
                    second_num = int(inputText[x + 1])
                except:
                    accumulator.setText('Format Error!')
                else:
                    inputText[x] = first_num / second_num
                    del inputText[x + 1]
                    del inputText[x - 1]
            elif (inputText[x] == '+'):
                try:
                    first_num = int(inputText[x - 1])
                    second_num = int(inputText[x + 1])
                except:
                    accumulator.setText('Format Error!')
                else:
                    inputText[x] = first_num + second_num
                    del inputText[x + 1]
                    del inputText[x - 1]
            elif (inputText[x] == '-'):
                try:
                    first_num = int(inputText[x - 1])
                    second_num = int(inputText[x + 1])
                except:
                    accumulator.setText('Format Error!')
                else:
                    inputText[x] = first_num - second_num
                    del inputText[x + 1]
                    del inputText[x - 1]
            else:
                x += 1
        accumulator.setText(str(inputText[0]))
    def clear_button_clicked(self):
        accumulator = self.window.findChild(QLineEdit, 'accumulatorText')
        currentText = accumulator.text()
        accumulator.setText('')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow('calculator.ui')
    sys.exit(app.exec_())


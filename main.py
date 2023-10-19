from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
import random

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_OK.clicked.connect(self.generate)

    def generate(self):
        s_number = '0123456789'
        s_alfabet = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
        pas = ''
        if self.ui.cl_number.isChecked():
            for i in range(16):
                pas = pas + random.choice(s_number)
        if self.ui.cl_alphabet.isChecked():
            for i in range(16):
                pas = pas + random.choice(s_alfabet)
        if self.ui.cl_number.isChecked() and self.ui.cl_alphabet.isChecked():
            for i in range(16):
                pas = pas + random.choice(s_number + s_alfabet)
        self.ui.result.setText(pas)
        


app = QApplication([])
window = Widget()


window.show()
app.exec_()

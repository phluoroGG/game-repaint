import
from PyQt5.QtWidgets import QMainWindow


class MyWindow(QMainWindow, window.Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.show()

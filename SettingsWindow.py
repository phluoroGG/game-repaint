from PyQt5.QtWidgets import QMainWindow, QMessageBox
from SettingsWindowUI import Ui_MainWindow


class SettingsWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(SettingsWindow, self).__init__(parent)
        self.setupUi(self)
        self.radioButtonAmateur.toggle()
        self.radioButtonCustom.toggled.connect(lambda: self.radio_checked())

    def closeEvent(self, event) -> None:
        if not self.radioButtonCustom.isChecked():
            event.accept()
        elif 4 <= int(self.lineEditWidth.text()) <= 30:
            if 4 <= int(self.lineEditHeight.text()) <= 30:
                if 3 <= int(self.lineEditColors.text()) <= 10:
                    event.accept()
                else:
                    QMessageBox.warning(self, 'Ошибка', 'Недопустимое значение количества цветов', QMessageBox.Ok)
                    event.ignore()
            else:
                QMessageBox.warning(self, 'Ошибка', 'Недопустимое значение высоты', QMessageBox.Ok)
                event.ignore()
        else:
            QMessageBox.warning(self, 'Ошибка', 'Недопустимое значение ширины ', QMessageBox.Ok)
            event.ignore()

    def radio_checked(self):
        if self.radioButtonCustom.isChecked():
            self.lineEditWidth.setEnabled(True)
            self.lineEditHeight.setEnabled(True)
            self.lineEditColors.setEnabled(True)
        else:
            self.lineEditWidth.setEnabled(False)
            self.lineEditHeight.setEnabled(False)
            self.lineEditColors.setEnabled(False)

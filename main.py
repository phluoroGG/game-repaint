import sys
import traceback

from PyQt5.QtWidgets import QApplication, QMessageBox
from MainWindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()


    def exception_hook(type_, value, tb):
        msg = '\n'.join(traceback.format_exception(type_, value, tb))
        QMessageBox.critical(mw, 'Unhandled top level exception', msg)

    sys.excepthook = exception_hook

    mw.show()
    sys.exit(app.exec_())

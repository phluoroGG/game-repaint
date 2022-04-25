from PyQt5 import QtCore
from PyQt5.QtCore import QModelIndex, Qt, QUrl
from PyQt5.QtGui import QPainter, QMouseEvent, QStandardItemModel, QColor
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QMainWindow, QItemDelegate, QStyleOptionViewItem

from MainWindowUI import Ui_MainWindow
from RepaintGame import *
from Settings import Settings
from SettingsWindow import SettingsWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self._settingsWindow = SettingsWindow(self)

        self._settings = Settings()
        self._game = RepaintGame(self._settings.row_count, self._settings.col_count, self._settings.color_count)

        self.game_resize(self._game, self._settings)

        class MyDelegate(QItemDelegate):
            def __init__(self, parent=None, *args):
                QItemDelegate.__init__(self, parent, *args)

            def paint(self, painter: QPainter, option: QStyleOptionViewItem, idx: QModelIndex):
                painter.save()
                self.parent().on_item_paint(idx, painter, option)
                painter.restore()

        self.gameFieldTableView.setItemDelegate(MyDelegate(self))

        class MyDelegate1(QItemDelegate):
            def __init__(self, parent=None, *args):
                QItemDelegate.__init__(self, parent, *args)

            def paint(self, painter: QPainter, option: QStyleOptionViewItem, idx: QModelIndex):
                painter.save()
                self.parent().on_item_paint1(idx, painter, option)
                painter.restore()

        self.colorButtonsTableView.setItemDelegate(MyDelegate1(self))

        def new_mouse_press_event(e: QMouseEvent) -> None:
            idx = self.colorButtonsTableView.indexAt(e.pos())
            if e.button() == Qt.LeftButton:
                self._game.left_mouse_click(list(colors.keys())[idx.column()])
            if self._game.state == RepaintGameState.WIN:
                self.setWindowTitle('Победа!')
            self.update_view()

        self.colorButtonsTableView.mousePressEvent = new_mouse_press_event
        self.actionNewGame.triggered.connect(self.on_new_game)
        self.actionSettings.triggered.connect(self.show_settings_window)
        self.actionExit.triggered.connect(self.close)
        self.actionAboutGame.triggered.connect(self.show_about_game_window)
        self.actionAboutAuthor.triggered.connect(self.show_about_author_window)

    def game_resize(self, game: RepaintGame, settings: Settings) -> None:
        model = QStandardItemModel(game.row_count, game.col_count)
        self.gameFieldTableView.setModel(model)
        model = QStandardItemModel(1, game.color_count)
        self.colorButtonsTableView.setModel(model)
        self.resize(35 * settings.row_count + 25, 30 * settings.col_count + 200)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 35 * settings.row_count + 102,
                                                             30 * settings.col_count + 152))
        self.gameFieldTableView.setFixedSize(35 * settings.row_count + 2, 30 * settings.col_count + 2)
        self.colorButtonsTableView.setFixedSize(50 * settings.color_count + 2, 50)

        self.update_view()

    def update_view(self):
        self.lcdNumber.display(self._game.turns)
        self.gameFieldTableView.viewport().update()

    def on_new_game(self):
        self.setWindowTitle('Перекраска')
        self.set_settings()
        self._game = RepaintGame(self._settings.row_count, self._settings.col_count, self._settings.color_count)
        self.game_resize(self._game, self._settings)
        self.update_view()

    def on_item_paint(self, e: QModelIndex, painter: QPainter, option: QStyleOptionViewItem) -> None:
        item = self._game[e.row(), e.column()]
        color = colors.get(item.color)
        painter.fillRect(option.rect, QColor(color.red, color.green, color.blue, 128))

    @staticmethod
    def on_item_paint1(e: QModelIndex, painter: QPainter, option: QStyleOptionViewItem) -> None:
        color = list(colors.values())[e.column()]
        painter.fillRect(option.rect, QColor(color.red, color.green, color.blue, 128))

    def set_settings(self):
        if self._settingsWindow.radioButtonNewbie.isChecked():
            self._settings.row_count = 8
            self._settings.col_count = 8
            self._settings.color_count = 4
        if self._settingsWindow.radioButtonAmateur.isChecked():
            self._settings.row_count = 12
            self._settings.col_count = 12
            self._settings.color_count = 6
        if self._settingsWindow.radioButtonProfessional.isChecked():
            self._settings.row_count = 20
            self._settings.col_count = 20
            self._settings.color_count = 10
        if self._settingsWindow.radioButtonCustom.isChecked():
            self._settings.row_count = int(self._settingsWindow.lineEditWidth.text())
            self._settings.col_count = int(self._settingsWindow.lineEditHeight.text())
            self._settings.color_count = int(self._settingsWindow.lineEditColors.text())

    def show_settings_window(self):
        self._settingsWindow.show()

    def show_about_game_window(self):
        global about_game
        about_game = QWebEngineView()
        about_game.load(QUrl.fromLocalFile('/AboutGame.html'))
        about_game.setWindowTitle('Об игре')
        about_game.show()

    def show_about_author_window(self):
        global about_author
        about_author = QWebEngineView()
        about_author.load(QUrl.fromLocalFile('/AboutAuthor.html'))
        about_author.setWindowTitle('Об авторе')
        about_author.show()


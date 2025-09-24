import pathlib
import sys
from pathlib import Path

from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QMainWindow, QFrame, QPushButton
from PySide6.QtCore import QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QIcon


class MainWindow(QMainWindow):
    """
    Main window class for connected widgets and controls.
    """

    def __init__(self):
        """
        Load window and connect widgets.
        """
        super().__init__()
        loader = QUiLoader()
        if getattr(sys, 'frozen', False):
            ui_file = Path(__file__).parent.parent.parent / "ui" / "main_window.ui"
        else:
            ui_file = Path(__file__).parent.parent / "ui" / "main_window.ui"
        self.ui = loader.load(ui_file)
        self.setCentralWidget(self.ui)

        # setup title and icon
        self.setWindowTitle("HDZero Programmer 2.0")
        icon_pth = pathlib.Path(__file__).parent.parent / "src" / "icons" / "HDZeroIcon.ico"
        self.setWindowIcon(QIcon(str(icon_pth)))

        # assign widgets objet with variables
        self.left_sidebar_frame = self.ui.findChild(QFrame, "left_sidebar_frame")
        self.btn_toggle_menu = self.ui.findChild(QPushButton, "btn_toggle_menu")

        # left sidebar run settings
        self.is_container_expanded = True
        self.expanded_width_on_start = 200

        # connect widgets with func
        self.btn_toggle_menu.clicked.connect(self.toggle_left_sidebar_frame_width)

    def toggle_left_sidebar_frame_width(self) -> None:
        """
        Animation sidebar

        :return: None
        """
        start_width = self.left_sidebar_frame.width()

        # setup animate properties
        if self.is_container_expanded:
            end_width = 58
        else:
            end_width = self.expanded_width_on_start

        # create animation properties
        self.animation = QPropertyAnimation(self.left_sidebar_frame, b"maximumWidth")
        self.animation.setDuration(300)
        self.animation.setStartValue(start_width)
        self.animation.setEndValue(end_width)
        self.animation.setEasingCurve(QEasingCurve.Type.InOutCubic)

        self.animation.start()

        self.is_container_expanded = not self.is_container_expanded

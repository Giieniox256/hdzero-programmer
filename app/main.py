from pathlib import Path
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QAction, QIcon


class MainWindow(QMainWindow):
    """
    Main window class for connected widgets and controls.
    """

    def __init__(self):
        """
        Constructor. Initialize a window.
        """
        super().__init__()
        loader = QUiLoader()
        main_window_path_file = Path(__file__).parent.parent / "ui/main_window.ui"
        icon_path = Path(__file__).parent.parent / "Images" / "HDZeroIcon.ico"
        self.main_window = loader.load(main_window_path_file)
        main_icon = QIcon(str(icon_path))
        self.main_window.setWindowIcon(main_icon)

        self.action_close_app = self.main_window.findChild(QAction, "actionClose")
        self.action_close_app.triggered.connect(self.close_app)

    def show(self):
        """
        Show the main window widget.
        :return:
        """
        self.main_window.show()

    def close_app(self):
        """
        Close the main window widget.
        :return:
        """
        self.main_window.close()

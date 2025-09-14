from pathlib import Path
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    """
    Main window class for connected widgets and controls.
    """

    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        main_window_path_file = Path(__file__).parent.parent / "ui/main_window.ui"
        self.main_window = loader.load(main_window_path_file)

    def show(self):
        self.main_window.show()

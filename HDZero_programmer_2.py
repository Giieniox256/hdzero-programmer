import sys
import resource.QrcFiles.image_resources
from PySide6.QtWidgets import QApplication
from app.main import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

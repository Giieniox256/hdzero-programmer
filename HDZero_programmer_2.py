import sys
from PySide6.QtWidgets import QApplication
### do not remove lines below!! ###
import src.resources
import PySide6.QtSvg
##########
from app.main import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

import sys

from PySide6.QtWidgets import QApplication

# from application.dependencies.schemas import some
from application.main_win import Application
# some()
if __name__ == '__main__':
    application = QApplication(sys.argv)
    application.setStyle('Fusion')
    window = Application()
    window.showMaximized()
    sys.exit(application.exec())

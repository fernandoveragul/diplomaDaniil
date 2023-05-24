import sys
from PySide6.QtWidgets import QApplication
from application.main_win import Application

if __name__ == '__main__':
    application = QApplication(sys.argv)
    window = Application()
    window.showMaximized()
    sys.exit(application.exec())

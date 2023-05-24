import sys
from PySide6.QtWidgets import QApplication
from application.main_win import Application
from qt_material import apply_stylesheet

if __name__ == '__main__':
    application = QApplication(sys.argv)
    window = Application()
    apply_stylesheet(application, theme='light_blue.xml')
    window.showMaximized()
    sys.exit(application.exec())

# ['dark_amber.xml',
#  'dark_blue.xml',
#  'dark_cyan.xml',
#  'dark_lightgreen.xml',
#  'dark_pink.xml',
#  'dark_purple.xml',
#  'dark_red.xml',
#  'dark_teal.xml',
#  'dark_yellow.xml',
#  'light_amber.xml',
#  'light_blue.xml',
#  'light_cyan.xml',
#  'light_cyan_500.xml',
#  'light_lightgreen.xml',
#  'light_pink.xml',
#  'light_purple.xml',
#  'light_red.xml',
#  'light_teal.xml',
#  'light_yellow.xml']
DESIGN_STYLE: str = """
QPushButton {
    border: 2px solid #8f8f91;
    border-radius: 4px;
    background-color: #e6daa6;
}
QPushButton:hover {
    background-color: #e6daa6, opacity 0,9;
}
QRadioButton::indicator::checked {
    background-color: #e6daa6;
    border-radius: 4px
    border: 2px solid #8f8f91
}
QTabBar::tab:selected  {
    background-color: #e6daa6;
    border: 2px solid #8f8f91;
    border-radius: 4px;
}  
QTabBar::tab:!selected {
    background-color: #e6daa6;
    border-radius: 4px;
}
QLineEdit {
    border: 2px solid #8f8f91;
    border-radius: 4px;
    background: #e6daa6;
}
"""
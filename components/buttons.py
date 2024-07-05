from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize

class GoToButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setObjectName('primary')

class SecondaryButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setObjectName('secondary')
        self.clicked.connect(self.on_click)

    def on_click(self):
        print('Botão Secundário clicado!')


class ItemButton(QPushButton):
    def __init__(self, icon_path, size=50, parent=None):
        super().__init__(parent)
        self.setObjectName('Icon')
        self.setIcon(QIcon(icon_path))
        self.setIconSize(QSize(24, 24))
        self.setFixedSize(size, size)  # Define o tamanho quadrado

from PySide6.QtWidgets import QPushButton

class PrimaryButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setObjectName('primary')
        self.clicked.connect(self.on_click)

    def on_click(self):
        print('Botão Principal clicado!')

class SecondaryButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setObjectName('secondary')
        self.clicked.connect(self.on_click)

    def on_click(self):
        print('Botão Secundário clicado!')

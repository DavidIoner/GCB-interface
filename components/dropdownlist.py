from PySide6.QtWidgets import QComboBox, QVBoxLayout, QWidget, QPushButton
from PySide6.QtGui import QIcon


class DropdownButtonWidget(QWidget):
    def __init__(self, items, parent=None):
        super().__init__(parent)

        # Cria o combo box
        self.combo_box = QComboBox()
        self.buttons = []

        # Adiciona os itens ao combo box e cria os botões correspondentes
        for item in items:
            self.combo_box.addItem(item['name'], item)
            button = QPushButton(item['name'])
            button.setIcon(QIcon(item['icon']))
            button.clicked.connect(item['onclick'])
            button.hide()
            self.buttons.append(button)

        # Conecta o evento de seleção do combo box a uma função
        self.combo_box.currentIndexChanged.connect(self.on_combobox_changed)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.combo_box)

        # Adiciona os botões ao layout
        for button in self.buttons:
            layout.addWidget(button)

        self.setLayout(layout)

    def on_combobox_changed(self, index):
        # Esconde todos os botões
        for button in self.buttons:
            button.hide()

        # Mostra o botão correspondente à opção selecionada
        # self.buttons[index].show()
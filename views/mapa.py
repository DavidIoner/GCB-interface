from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy
from PySide6.QtCore import Qt, QTimer
import os
from buttons import GoToButton, SecondaryButton
from utils import save_geometry, set_screen_geometry, apply_stylesheet
from components.dropdownlist import DropdownButtonWidget

class Mapa(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        items = [
            {"name": "Opção 1", "icon": "assets/dht.png", "onclick": self.on_button1_click},
            {"name": "Opção 2", "icon": "assets/dht.png", "onclick": self.on_button2_click},
            {"name": "Opção 3", "icon": "assets/dht.png", "onclick": self.on_button3_click}
        ]


        main_layout = QVBoxLayout()
        # Cria o widget da dropdown list
        self.dropdown_widget = DropdownButtonWidget(items)

        main_layout.addWidget(self.dropdown_widget)
        # Layout horizontal para os botões
        button_layout = QHBoxLayout()

        # Adicionar botões usando classes específicas
        btn_primary = GoToButton('Ir para Segunda Tela', self)
        btn_primary.clicked.connect(self.go_to_second_view)
        button_layout.addWidget(btn_primary)
        # Adicionar um espaçador 
        button_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        
        main_layout.addStretch()
        main_layout.addLayout(button_layout)


        self.setLayout(main_layout)
        self.setWindowTitle('Mapa')

        # Ler o arquivo de estilo e aplicar
        apply_stylesheet(self, 'styles.qss')

        # Restaurar a posição e o tamanho da janela
        # restore_geometry(self)
        set_screen_geometry(self, "max")
        

    def on_button1_click(self):
        print("Botão 1 clicado")

    def on_button2_click(self):
        print("Botão 2 clicado")

    def on_button3_click(self):
        print("Botão 3 clicado")

    def closeEvent(self, event):
        save_geometry(self)
        event.accept()

    def go_to_second_view(self):
        from views.second_view import SecondView  # Importação movida para dentro do método
        self.second_view = SecondView()
        
        # Mostrar a nova tela primeiro
        self.second_view.show()

        # Fechar a tela atual somente depois que a nova estiver visível
        QTimer.singleShot(1000, self.close)

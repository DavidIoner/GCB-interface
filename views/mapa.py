from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy
from PySide6.QtCore import Qt, QTimer
import os
from buttons import PrimaryButton, SecondaryButton
from utils import save_geometry, set_screen_geometry

class Mapa(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()

        # Layout horizontal para os botões
        button_layout = QHBoxLayout()

        # Adicionar botões usando classes específicas
        btn_primary = PrimaryButton('Ir para Segunda Tela', self)
        btn_primary.clicked.connect(self.go_to_second_view)
        button_layout.addWidget(btn_primary)

        # Adicionar um espaçador para empurrar os botões para o lado esquerdo
        button_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # Adicionar o layout de botões ao layout principal
        main_layout.addStretch()
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)
        self.setWindowTitle('Mapa')

        # Ler o arquivo de estilo e aplicar
        self.apply_stylesheet('styles.qss')

        # Restaurar a posição e o tamanho da janela
        # restore_geometry(self)
        set_screen_geometry(self, "max")

    def apply_stylesheet(self, stylesheet_path):
        if os.path.exists(stylesheet_path):
            with open(stylesheet_path, 'r') as file:
                stylesheet = file.read()
                self.setStyleSheet(stylesheet)
        else:
            print(f"Arquivo de estilo '{stylesheet_path}' não encontrado.")

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

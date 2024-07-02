from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
import os

class MultiButtonSimulator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Botão principal com estilo "primary"
        btn_primary = QPushButton('Botão Principal', self)
        btn_primary.setObjectName('primary')
        btn_primary.clicked.connect(self.on_primary_click)
        layout.addWidget(btn_primary)

        # Botão secundário com estilo "secondary"
        btn_secondary = QPushButton('Botão Secundário', self)
        btn_secondary.setObjectName('secondary')
        btn_secondary.clicked.connect(self.on_secondary_click)
        layout.addWidget(btn_secondary)

        self.setLayout(layout)
        self.setWindowTitle('Botões com Estilos Diferentes')

        # Ler o arquivo de estilo e aplicar
        self.apply_stylesheet('styles.qss')

        

        # Configurar a janela para tela cheia sem bordas
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # self.showFullScreen()
        self.show()

    def apply_stylesheet(self, stylesheet_path):
        if os.path.exists(stylesheet_path):
            with open(stylesheet_path, 'r') as file:
                stylesheet = file.read()
                self.setStyleSheet(stylesheet)
        else:
            print(f"Arquivo de estilo '{stylesheet_path}' não encontrado.")

    def on_primary_click(self):
        print('Botão Principal clicado!')

    def on_secondary_click(self):
        print('Botão Secundário clicado!')

if __name__ == '__main__':
    app = QApplication([])
    ex = MultiButtonSimulator()
    app.exec_()

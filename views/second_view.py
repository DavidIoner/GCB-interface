from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from utils import  save_geometry, set_screen_geometry
from PySide6.QtCore import QTimer

class SecondView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Botão para voltar à tela principal
        btn_back = QPushButton('Voltar para Mapa', self)
        btn_back.clicked.connect(self.go_to_main_view)
        layout.addWidget(btn_back)

        self.setLayout(layout)
        self.setWindowTitle('Segunda Tela')

        # Restaurar a posição e o tamanho da janela
        set_screen_geometry(self, "max")

    def closeEvent(self, event):
        save_geometry(self)
        event.accept()

    def go_to_main_view(self):
        from views.mapa import Mapa  # Importação movida para dentro do método
        self.main_view = Mapa()
        
        # Mostrar a nova tela primeiro
        self.main_view.show()

        # Fechar a tela atual somente depois que a nova estiver visível
        QTimer.singleShot(1000, self.close)

from PySide6.QtWidgets import QWidget, QVBoxLayout, QSpacerItem, QSizePolicy, QHBoxLayout
from utils.screen_size import  save_geometry, set_screen_geometry, apply_stylesheet
from PySide6.QtCore import QTimer
from components.buttons import GoToButton

class SecondView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        button_layout = QHBoxLayout()

        # Botão para voltar à tela principal
        btn_back = GoToButton('Voltar para Mapa', self)
        btn_back.clicked.connect(self.go_to_main_view)
        button_layout.addWidget(btn_back)
        # Adicionar um espaçador 
        button_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.setLayout(layout)
        self.setWindowTitle('Segunda Tela')
        layout.addStretch()
        layout.addLayout(button_layout)


        # Restaurar a posição e o tamanho da janela
        set_screen_geometry(self, "max")
        apply_stylesheet(self, 'styles.qss')


    def closeEvent(self, event):
        save_geometry(self)
        event.accept()

    def go_to_main_view(self):
        from views.mapa import Mapa  # Importação movida para dentro do método
        self.main_view = Mapa()
        
        # Mostrar a nova tela primeiro
        self.main_view.show()

        # Fechar a tela atual somente depois que a nova estiver visível
        QTimer.singleShot(500, self.close)

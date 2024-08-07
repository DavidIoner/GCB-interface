from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QMainWindow, QGraphicsScene, QGraphicsPixmapItem, QPushButton, QFrame
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QPixmap
from components.buttons import GoToButton
from utils.screen_size import save_geometry, set_screen_geometry, apply_stylesheet
from components.dropdownlist import DropdownButtonWidget
from components.buttons import ItemButton
from components.image import GraphicsView

class Mapa(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        items = [
            {"name": "Opção 1", "icon": "assets/dht.png", "onclick": self.on_button1_click},
            {"name": "Opção 2", "icon": "assets/dht.png", "onclick": self.on_button2_click},
            {"name": "Opção 3", "icon": "assets/dht.png", "onclick": self.on_button3_click}
        ]

        # Cria o widget principal e define o layout principal
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.main_layout = QVBoxLayout(central_widget)

        # Configurar QGraphicsView e QGraphicsScene
        self.graphics_view = GraphicsView(self)
        self.graphics_scene = QGraphicsScene(self)
        self.graphics_view.setScene(self.graphics_scene)
        
        # Carregar a imagem e adicionar à cena
        self.pixmap = QPixmap("assets/image.png")  # Caminho da imagem
        if not self.pixmap.isNull():
            self.pixmap_item = QGraphicsPixmapItem(self.pixmap)
            self.graphics_scene.addItem(self.pixmap_item)
        else:
            print("Failed to load image")

        # Adicionar GraphicsView ao layout principal
        self.main_layout.addWidget(self.graphics_view)

        # Widget da barra lateral
        self.left_bar = QWidget(self)
        left_bar_layout = QVBoxLayout()
        left_bar_layout.addWidget(QPushButton("Button 1"))
        left_bar_layout.addWidget(QPushButton("Button 2"))
        self.left_bar.setLayout(left_bar_layout)
        self.left_bar.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.left_bar.setFixedWidth(150)  # Definir uma largura fixa para a barra lateral

        # Definir a cor azul com transparência para a barra lateral
        self.left_bar.setStyleSheet("background-color: rgba(0, 0, 255, 150);")  # Azul com transparência

        # Adicionar um QFrame para criar uma sobreposição
        self.overlay_frame = QFrame(self)
        self.overlay_frame.setLayout(QVBoxLayout())
        self.overlay_frame.layout().addWidget(self.left_bar)
        self.overlay_frame.setStyleSheet("background: rgba(0, 0, 0, 0);")  # Tornar o fundo transparente
        self.overlay_frame.setGeometry(0, 0, 150, self.height())  # Ajuste conforme necessário
        self.overlay_frame.setAttribute(Qt.WA_TranslucentBackground)  # Para permitir fundo transparente

        self.setWindowTitle('Mapa')

        # Restaurar a posição e o tamanho da janela
        set_screen_geometry(self, "full")

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.overlay_frame.setGeometry(0, 0, 150, self.height())  # Atualizar a geometria na mudança de tamanho

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
        QTimer.singleShot(500, self.close)

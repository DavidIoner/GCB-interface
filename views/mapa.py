from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QMainWindow
from PySide6.QtCore import QTimer
from components.buttons import GoToButton
from utils.screen_size import save_geometry, set_screen_geometry, apply_stylesheet
from components.dropdownlist import DropdownButtonWidget
from components.buttons import ItemButton
from components.image import ImageViewer



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


        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)
        lateral_layout = QHBoxLayout()
        # Cria o widget da dropdown list
        self.dropdown_widget = DropdownButtonWidget(items)

        main_layout.addWidget(self.dropdown_widget)
        main_layout.addLayout(lateral_layout)

        # Layout vertical esquerdo
        left_layout = QVBoxLayout()
        left_layout.setSpacing(8)
        left_widget = QWidget()
        left_widget.setLayout(left_layout)
        lateral_layout.addWidget(left_widget)



        central_layout = QVBoxLayout()
        central_widget_inner = QWidget()
        central_widget_inner.setLayout(central_layout)
        lateral_layout.addWidget(central_widget_inner)

        image_viewer = ImageViewer("assets/image.png")
        central_layout.addWidget(image_viewer)
        


        # Layout vertical direito
        right_layout = QVBoxLayout()
        right_layout.setSpacing(8)
        right_widget = QWidget()
        right_widget.setLayout(right_layout)
        lateral_layout.addWidget(right_widget)


        for _ in range(5):
            button = ItemButton("assets/test.svg")
            button.clicked.connect(self.on_button1_click)
            left_layout.addWidget(button)


        # btn_item = ItemButton("assets/test.svg")
        # btn_item.clicked.connect(self.on_button1_click)
        # button_layout.addWidget(btn_item)

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
        QTimer.singleShot(500, self.close)

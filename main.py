from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class MaterialButtonSimulator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        btn = QPushButton('Clique', self)
        btn.setStyleSheet("""
            QPushButton {
                background-color: #6200EE;  /* Primary color */
                color: white;               /* White text */
                border: none;               /* No border */
                border-radius: 4px;         /* Rounded corners */
                padding: 16px 24px;         /* Padding */
                font-size: 14px;            /* Font size */
                text-transform: uppercase;  /* Uppercase text */
                box-shadow: 0px 2px 2px rgba(0, 0, 0, 0.2); /* Shadow */
                transition: background-color 0.3s ease;  /* Smooth transition */
            }
            QPushButton:hover {
                background-color: #3700B3;  /* Darker primary on hover */
            }
        """)
        btn.clicked.connect(self.on_click)
        layout.addWidget(btn)

        self.setLayout(layout)
        self.setWindowTitle('Material Design Button')
        self.show()

    def on_click(self):
        print('Botão clicado!')

if __name__ == '__main__':
    app = QApplication([])
    ex = MaterialButtonSimulator()
    app.exec_()
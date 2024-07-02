from PySide6.QtWidgets import QApplication
from views.mapa import Mapa

if __name__ == '__main__':
    app = QApplication([])
    ex = Mapa()
    ex.show()
    app.exec()

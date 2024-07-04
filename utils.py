from PySide6.QtCore import QSettings, Qt
import os


def restore_geometry(widget):
    settings = QSettings("MyCompany", "MyApp")
    geometry = settings.value("geometry")
    if geometry:
        widget.restoreGeometry(geometry)

def save_geometry(widget):
    settings = QSettings("MyCompany", "MyApp")
    settings.setValue("geometry", widget.saveGeometry())

def fullscren_no_border(widget):
    widget.setWindowFlags(Qt.FramelessWindowHint)
    widget.showFullScreen()

def set_screen_geometry(widget, type="full"):
    if type == "full":
        fullscren_no_border(widget)
    elif type == "max":
        widget.showMaximized()
    elif type == "restore":
        restore_geometry(widget)


def apply_stylesheet(widget, stylesheet_path):
    if os.path.exists(stylesheet_path):
        with open(stylesheet_path, 'r') as file:
            stylesheet = file.read()
            widget.setStyleSheet(stylesheet)
    else:
        print(f"Arquivo de estilo '{stylesheet_path}' não encontrado.")
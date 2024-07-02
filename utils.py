from PySide6.QtCore import QSettings, Qt

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



import os
import PyQt5
# Чтобы работал PyQt5
pyqt_path = os.path.dirname(PyQt5.__file__)
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.join(pyqt_path, "Qt5", "plugins", "platforms")



# КОД ПРИЛОЖЕНИЯ
from PyQt5.QtWidgets import (
    QApplication, QWidget
)

app = QApplication([])
window = QWidget()

window.show()
app.exec()
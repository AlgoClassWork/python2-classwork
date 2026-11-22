import os
import PyQt5
# Чтобы работал PyQt5
pyqt_path = os.path.dirname(PyQt5.__file__)
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.join(pyqt_path, "Qt5", "plugins", "platforms")



# КОД ПРИЛОЖЕНИЯ
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout
)

app = QApplication([])
window = QWidget()
question = QLabel('Какого цвета чернокожие?')
question.setStyleSheet('font-size:50px ; color:red')
line = QVBoxLayout()
line.addWidget(question)


window.setLayout(line)
window.show()
app.exec()

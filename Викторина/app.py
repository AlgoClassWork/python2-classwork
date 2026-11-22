import os
import PyQt5

# Чтобы работал PyQt5
pyqt_path = os.path.dirname(PyQt5.__file__)
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.join(pyqt_path, "Qt5", "plugins", "platforms")



# КОД ПРИЛОЖЕНИЯ
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout
)

# Создание обьектов интерфейса
app = QApplication([])
window = QWidget()

question = QLabel('Какого цвета чернокожие?')
button1 = QPushButton('Красные')
button2 = QPushButton('Белые')
button3 = QPushButton('Черные')
button4 = QPushButton('Синие')

# Стилизация обьектов интерфейса
question.setStyleSheet('font-size:40px')
button1.setStyleSheet('font-size:30px ; color:red')
button2.setStyleSheet('font-size:30px ; color:white')
button3.setStyleSheet('font-size:30px ; color:black')
button4.setStyleSheet('font-size:30px ; color:blue')

# Размещение обьектов интерфейса
line = QVBoxLayout()
h_line1 = QHBoxLayout()
h_line2 = QHBoxLayout()


line.addWidget(question)
line.addLayout(h_line1)
line.addLayout(h_line2)
h_line1.addWidget(button1)
h_line1.addWidget(button2)
h_line2.addWidget(button3)
h_line2.addWidget(button4)

window.setLayout(line)

# Реакции на события
def test():
    print('кто то нажал на кнопку')

# Подписки на события
button1.clicked.connect(test)

# Запуск приложения
window.show()
app.exec()

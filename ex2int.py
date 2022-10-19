import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel

app = QApplication(sys.argv)

janela = QWidget()
janela.resize(500, 300)
janela.setWindowTitle("CruTube")

btn = QPushButton("botao 1",janela)
btn.setGeometry(100, 100, 150, 80)
btn.setStyleSheet('color:blue')#letra
btn.setStyleSheet('background-color:blue; color:red')#background

label = QLabel("TESTE",janela)
label.move(400, 100)



janela.show()

app.exec()
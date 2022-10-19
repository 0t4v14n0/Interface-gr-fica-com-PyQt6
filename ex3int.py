import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel

def funcao1():
    label.setText("botao 1 foi clicado")
    label.adjustSize()

def funcao2():
    label.setText("botao 2 foi clicado")
    label.adjustSize()

app = QApplication(sys.argv)

janela = QWidget()
janela.resize(500, 300)
janela.setWindowTitle("CruTube")

btn = QPushButton("botao 1",janela)
btn.setGeometry(50, 100, 150, 80)
btn.setStyleSheet('color:blue')#letra
btn.setStyleSheet('background-color:white; color:red')#background
btn.clicked.connect(funcao1)

btn2 = QPushButton("botao 2",janela)
btn2.setGeometry(200, 100, 150, 80)
btn2.setStyleSheet('color:blue')#letra
btn2.setStyleSheet('background-color:white; color:red')#background
btn2.clicked.connect(funcao2)

label = QLabel("TESTE",janela)
label.move(200, 200)
label.setStyleSheet('font-size:35px')

janela.show()

app.exec()
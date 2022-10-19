import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit

def funcao1():
    label.setText("botao 1 foi clicado")
    label.adjustSize()

def funcao2():
    label.setText("botao 2 foi clicado")
    label.adjustSize()

def funcao3():
    vl = le.text()
    label.setText(vl)
    label.adjustSize()

app = QApplication(sys.argv)

janela = QWidget()
janela.resize(500, 300)
janela.setWindowTitle("CruTube")

btn = QPushButton("botao 1",janela)
btn.setGeometry(25, 100, 150, 80)
btn.setStyleSheet('background-color:white; color:red')#background
btn.clicked.connect(funcao1)

btn2 = QPushButton("botao 2",janela)
btn2.setGeometry(175, 100, 150, 80)
btn2.setStyleSheet('background-color:white; color:red')#background
btn2.clicked.connect(funcao2)

btn3 = QPushButton("botao 3",janela)
btn3.setGeometry(325, 100, 150, 80)
btn3.setStyleSheet('background-color:white; color:red')#background
btn3.clicked.connect(funcao3)

label = QLabel("TESTE",janela)
label.move(150, 200)
label.setStyleSheet('font-size:30px')

le = QLineEdit("",janela)
le.setGeometry(175, 10 , 150, 40)

janela.show()

app.exec()
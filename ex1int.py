import sys

from PyQt6.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

janela = QWidget()
janela.resize(500,300)
janela.setWindowTitle("CruTube")
janela.show()

app.exec()
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from memo_edit_layout import *
from programm import *
app = QApplication([])
win = QWidget()
win.setFixedSize(1000,500)
win.move(0,0)
win.setLayout(main_edir_layout)
#main
#main_edir_layout
































win.show()
app.exec_()
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import randint
from time import *
def show_ans():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button.clicked.connect(show_quast)
def show_quast():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    button.clicked.connect(show_ans)
app = QApplication([])
win = QWidget()
win.setWindowTitle("Memory Card")
win.move(30,60)
win.resize(600,500)


RadioGroupBox = QGroupBox("Варіанти відповідей")
RadioGroup = QButtonGroup()

scrin = QLabel("яблоко")
button = QPushButton("answer")
menu = QPushButton("menu")
chill = QPushButton("relax")
spin_box = QSpinBox()
spin_box.setValue(30)
min = QLabel("Хвилин")
ans1 = QRadioButton("apple")
ans2 = QRadioButton("application")
ans3 = QRadioButton("building")
ans4 = QRadioButton("caterpillar")
ans_layoutV = QVBoxLayout()
ans_layoutH1 = QHBoxLayout()
ans_layoutH2 = QHBoxLayout()

ans_layoutH1.addWidget(ans1,alignment = Qt.AlignCenter)
ans_layoutH1.addWidget(ans2,alignment = Qt.AlignCenter)
ans_layoutH2.addWidget(ans3,alignment = Qt.AlignCenter)
ans_layoutH2.addWidget(ans4,alignment = Qt.AlignCenter)
RadioGroup.addButton(ans1)
RadioGroup.addButton(ans2)
RadioGroup.addButton(ans3)
RadioGroup.addButton(ans4)

ans_layoutV.addLayout(ans_layoutH1)
ans_layoutV.addLayout(ans_layoutH2)

RadioGroupBox.setLayout(ans_layoutV)

AnsGroupBox = QGroupBox("test results")
Result = QLabel("Win")
Correct = QLabel("Loose")
layout_res = QVBoxLayout()
layout_res.addWidget(Result,alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(Correct,alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()

main = QVBoxLayout()
lay1 = QHBoxLayout()
lay2 = QHBoxLayout()
lay3 = QHBoxLayout()
lay4 = QHBoxLayout()

lay1.addWidget(menu, alignment = Qt.AlignLeft)
lay1.addWidget(chill, alignment = Qt.AlignRight)
lay1.addWidget(spin_box, alignment = Qt.AlignRight)
lay1.addWidget(min, alignment = Qt.AlignRight)
lay2.addWidget(scrin, alignment = Qt.AlignCenter)
lay3.addWidget(RadioGroupBox, alignment = Qt.AlignCenter)
lay4.addWidget(button, alignment = Qt.AlignCenter)


        
main.addLayout(lay1)
main.addLayout(lay2)
main.addLayout(lay3)
main.addLayout(lay4)

win.setLayout(main)




button.clicked.connect(show_ans)





































win.show()
app.exec_()

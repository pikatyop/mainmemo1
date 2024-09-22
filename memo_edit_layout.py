from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
app = QApplication([])
win = QWidget()
win.setFixedSize(1000,500)
win.move(0,0)

main_edir_layout = QVBoxLayout()
up_layoutH = QHBoxLayout()
list_view = QListView()
up_layoutH.addWidget(list_view)


txt_Quest = QLineEdit('')
txt_Ans = QLineEdit('')
txt_Wrong_ans = QLineEdit('')
txt_Wrong_ans2 = QLineEdit('')
txt_Wrong_ans3 = QLineEdit('')

startbutt = QPushButton("Почати тренування")
createbutt = QPushButton("Нове тренування")
savebutt = QPushButton("Записати відповідь")
butt = QPushButton("test")
layout_form =  QFormLayout()
layout_form.addRow("Quest:",txt_Quest)
layout_form.addRow("Ans:",txt_Ans)
layout_form.addRow("Wrong_ans:",txt_Wrong_ans)
layout_form.addRow("Wrong_ans2:",txt_Wrong_ans2)
layout_form.addRow("Wrong_ans3:",txt_Wrong_ans3)
up_layoutH.addLayout(layout_form)
main_edir_layout.addLayout(up_layoutH)
down_LayoutH = QHBoxLayout()
down_LayoutH.addWidget(createbutt)
down_LayoutH.addWidget(savebutt)
main_edir_layout.addLayout(down_LayoutH)
main_edir_layout.addWidget(startbutt)

win.setLayout(main_edir_layout)
















win.show()
app.exec_()



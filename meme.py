class Form():
    def __init__(self,quest = '', ans = '', wrong_ans = '', wrong_ans2 = '', wrong_ans3 = ''):
        self.quest = quest
        self.ans = ans
        self.wrong_ans = wrong_ans
        self.wrong_ans2 = wrong_ans2
        self.wrong_ans3 = wrong_ans3

class FormView():
    def __init__(self,quest = '', ans = '', wrong_ans = '', wrong_ans2 = '', wrong_ans3 = ''):
        self.quest = quest
        self.ans = ans
        self.wrong_ans = wrong_ans
        self.wrong_ans2 = wrong_ans2
        self.wrong_ans3 = wrong_ans3
    def show(self):
        print(self.quest)
        print(self.ans)
        print(self.wrong_ans)
        print(self.wrong_ans2)
        print(self.wrong_ans3)




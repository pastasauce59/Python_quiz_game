class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def next_question(self): 
        q_num = self.question_number
        question = self.question_list[q_num]
        q_num += 1
        input(f'Q.{q_num}: {question.text} (True/False)?: ')
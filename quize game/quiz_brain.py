class QuizeBrain:
    def __init__(self,question_list):
        self.question_number=0
        self.score=0
        self.question_list=question_list

    def next_question(self):
        current_question= self.question_list[self.question_number]
        self.question_number+=1
        user_answer=input(f"Q.n.{self.question_number}. {current_question.text} (true/false): ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_question(self):
        return self.question_number< len(self.question_list)
    
    def check_answer(self,user_answer, correct_answer):
        if user_answer.lower()==correct_answer.lower():
            self.score+=1
            print("you got ir right!")
        else:
            print("you're wrong!")
        print(f"the correct answer is {correct_answer}")
        print(f"your score is {self.score}/{self.question_number}")
        print("\n")


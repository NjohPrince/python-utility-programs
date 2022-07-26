class QuizBrain:
    def __init__(self, question_list):
        self.score = 0
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text}, True or False? ")
        self.check_answer(user_answer.lower(), current_question.answer.lower())

    def has_next_question(self):
        """
        Return true if quiz has got more questions
        """
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer != "true" and user_answer != "false":
            self.question_number -= 1
            return
        if user_answer == correct_answer:
            self.score += 1
            print(f"You got it right!")
        else:
            print("That's wrong")
        print(f"The correct answer was: {correct_answer.title()}")
        print(f"Your current score is: {self.score}/{self.question_number}.\n ")

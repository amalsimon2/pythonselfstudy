import json

class QuizApp:
    def __init__(self, questions_file):
        with open(questions_file, 'r') as file:
            self.questions = json.load(file)
        self.score = 0

    def run(self):
        print("Welcome to the Quiz App!")
        for question in self.questions:
            print(question['question'])
            for i, option in enumerate(question['options']):
                print(f"{i + 1}. {option}")
            user_answer = input("Enter your answer (1-4): ").strip()
            if user_answer.isdigit() and int(user_answer) == question['answer'] - 1:
                self.score += 1
        print(f"Quiz completed! Your score: {self.score}/{len(self.questions)}")

if __name__ == '__main__':
    quiz = QuizApp('questions.json')
    quiz.run()

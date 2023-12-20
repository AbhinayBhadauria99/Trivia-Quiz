from question_model import Question
from ui import QuizInterface
from quiz_brain import QuizBrain
import requests

response = requests.get(url="https://opentdb.com/api.php?amount=10&category=18&type=boolean")
response.raise_for_status()
data=response.json()

question_bank = []
for question in data["results"]:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_UI = QuizInterface(quiz)

#while quiz.still_has_questions():
#   quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

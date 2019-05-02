from Question import Question
from two_sum import Solution

question_prompts = [
    "What color are Apples? \n(a) Red/Green\n(b) Yellow\n(c) Blue\n\n" ,
    "What color are Bananas? \n(a) Red/Green\n(b) Yellow\n(c) Blue\n\n" ,
    "What color are Blueberries? \n(a) Red/Green\n(b) Yellow\n(c) Blue\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score +=1
    print("You got " + str(score) + "/" + str(len(questions)) + "correct")

run_test(questions)


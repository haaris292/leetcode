from hashmap import Questins

ques = [
    "what color is mango? \n(a) Yellow\n(b) Blue\n\n",
    "what color is orange? \n(a) orange\n(b) Blue\n\n",
    "what color is papaya? \n(a) Yellow\n(b) Blue\n\n"
]

asking = [
    Questins(ques[0], "a"),
    Questins(ques[1], "a"),
    Questins(ques[2], "a"),
]

def furit_app(asking):
    score = 0
    for i in asking:
        ans = input(i.prompt)
        if ans == i.answer:
            score +=1
    print("You got " + str(score) + "out of " +str(len(ques)) + "correct")

furit_app(asking)
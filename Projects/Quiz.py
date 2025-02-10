#Quiz Game#
import time

Questions = (("How many elements in the periodic table?"),
             ("Which animal lays the largest eggs?"),
             ("What is the most abundant gas in Earth's atmosphere?"),
             ("How many bones are in the human body?"),
             ("Which planet in the solar system is the hottest?"))
Options = (("A.116","B.117","C.118","D.119"),
           ("A.Whale","B.Crocodile","C.Elephant","D.Ostrich"),
           ("A.Nitrogen","B.Oxygen","C.Carbon-Dioxide","D.Hydrogen"),
           ("A.206","B.207","C.208","D.209"),
           ("A.Mercury","B.Venus","C.Earth","D.Mars"))
Answers = ("C","D","A","A","B")
Guesses = []
Score = 0
Question_number = 0

for Question in Questions:
    print(f"-------------Question{Question_number}-------------")
    print(Question)
    for Option in Options[Question_number]:
        print(Option)

    Guess = input("Enter Your Answer:").upper()
    Guesses.append(Guess)
    if Guess == Answers[Question_number]:
        Score += 1
        print("Correct")
    else:
        print("Incorrect")
        print(f"{Answers[Question_number]} is the correct answer")
    Question_number += 1
    time.sleep(1)


print("-----------------------")
print("RESULT")
print("-----------------------")

print("Answers:        Guesses:",end="\n")
for Answer,Guess in zip(Answers,Guesses):
    print(Answer,"                  ",Guess,end="\n")


print("-----------------------")
print("Score:",int(Score/len(Questions)*100))
print("-----------------------")
text = "Welcome to the \033[31mStar Wars\033[0m survey!"
middle = text.center(130)
print(middle)
print("You think you are experienced enough by just watching the films?")
print()
response = int(input("Yes or No? (\033[31m1\033[0m or \033[31m2\033[0m): "))
if response  == 1:
    print("Alright then, lets go!")
    print()
elif response  == 2:
    input("Alright then, cya! \033[33mGod bless you!\033[0m")
else:
    input("Sorry! Didn't understood your input.")

score = 0   #Zählt die Richtig gelösenen Fragen
mistakes1 = 0   #Zählt die mistakes

class Quizzes:
    def __init__(self, oi1, oi2, oi3):
        self.answer1 = oi1  #Nicht vergessen, "self" ist das Objekt. In dem programm "Quiz1"!
        self.answer2 = oi2
        self.answer3 = oi3


Quiz1 = Quizzes("Yoda", "Jango Fett", "General Grievous")
Quiz2 = Quizzes("Mustafar", "Kamino", "Endor")
Quiz3 = Quizzes("Emperor Palpatine", "Mace Windu", "Qui-Gon Jinn")

print("Question \033[31m1\033[0m: \033[36mWho is a Jedi Master in the prequel trilogy?\033[0m")
for ls1 in ["(1): Yoda ", "(2): Jango Fett", "(3): General Grievous"]:
    print(ls1)
asw1 = int(input("Answer (\033[31m1,2 or 3\033[0m): "))
while asw1 != 1:
    if asw1 == 2:
        print("Nope! Try again! ")
    elif asw1 == 3:
        print("Nope! Try again! ")
    elif asw1 != int:
        print("That's not an option! Please choose between 1,2 and 3.")
    mistakes1 += 1
    asw1 = int(input("Answer (\033[31m1,2 or 3\033[0m): "))

print(f"Correct! The answer was :{Quiz1.answer1}!")
score += 1      #dem score einen punkt zuweisen :D
print("")
print("Up to the second Question!:")
mistakes2 = 0
print("\033[36mWhich planets are featured in Return of the Jedi?\033[0m")
for ls2 in ["(1) Mustafar", "(2) Kamino", "(3) Endor"]:
    print(ls2)
asw2 = int(input("Answer (\033[31m1,2 or 3\033[0m): "))
while asw2 != 3:
    if asw2 == 1:
        print("Nope! Try again!")
    elif asw2 == 2:
        print("Nope! Try again!")
    elif asw2 != int:
        print("That's not an option! Please choose between 1,2 and 3.")
    mistakes2 += 1
    asw2 = int(input("Answer (\033[31m1,2 or 3\033[0m): "))

print(f"Correct! Keep goin! The answer was: {Quiz2.answer3}")
score += 1
print("Now to the last question...")
print("")
print("\033[36mWho are Sith Lords in the Skywalker saga?\033[0m")
for ls3 in ["(1) Emperor Palpatine", "(2) Mace Windu", "(3) Qui-Gon Jinn"]:
    print(ls3)
asw3 = int(input("Answer (\033[31m1,2 or 3\033[0m): "))
mistakes3 = 0
while asw3 != 1:
    if asw3 == 2:
        print("Yikes! Good guess but its false, try again!")
    elif asw3 == 3:
        print("Nopeeee, try again bro. I know you can do it!")
    elif asw3 != int:
        print("That's not an option! Please choose between 1,2 and 3.")
    mistakes3 += 1
    asw3 = int(input("Answer (\033[31m1,2 or 3\033[0m): "))
print(f"Correct!! The answer was: {Quiz3.answer1}. \033[33mGod bless you\033[0m, Congratulation!")
score += 1
print("")
print("")
print(f"Your score points: {score}.")
calculated_mistakes = mistakes1 + mistakes2+ mistakes3
print(f"Your mistakes: {calculated_mistakes}.")
print()
print()
print("Thanks for playing! Check out my other projects as well!")
print("\033[33mGod Bless you!\033[0m")





input("Press any key to end the programm...")















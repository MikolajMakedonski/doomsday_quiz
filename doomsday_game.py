import datetime
import random
userScore = 0

def get_input(prompt = "", cast = None, condition = None, errorMessage = None):
    while True:
        try:
            response = cast(input(prompt))
            assert condition is None or condition(response)
            return response
        except:
            print(errorMessage)

print("Hi, welcome to The doomsday calculation game!")
difficultyLevel = get_input(prompt = """Please choose the number associated with the desired difficulty level:
                                        \n1. Begginner (1900-2099)\n2. Intermediate (1800-2199)\n3. Hard (1-9999)\n,"""
                        cast = int,
                        condition = lambda y: 4 > y > 0,
                        errorMessage = "Please enter the difficulty 1-3.")
questionAmount = get_input(prompt = "How many times do you want to guess?\n",
                        cast = int,
                        condition = lambda y: y > 0,
                        errorMessage = "Please choose a valid number of questions desired.")

if difficultyLevel == 1:
    startDate = datetime.date(1900, 1, 1)
    endDate = datetime.date(2099, 12, 31)
elif difficultyLevel == 2:
    startDate = datetime.date(1800, 1, 1)
    endDate = datetime.date(2199, 12, 31)
elif difficultyLevel == 3:
    startDate = datetime.date(1, 1, 1)
    endDate = datetime.date(9999, 12, 31)

datesSpan = endDate - startDate
daysBetweenDates = datesSpan.days

print("""Rule: For a random date, you answer what day of the week that is:\n
      0-Sunday 1-Monday 2-Tuesday 3-Wednesday 4-Thursday 5-Friday 6-Saturday""")
for x in range(questionAmount):
    randomizedNumberOfDays = random.randrange(0, daysBetweenDates)
    pseudoRandomDate = startDate + datetime.timedelta(days = randomizedNumberOfDays)
    print("Your date to guess is", pseudoRandomDate.strftime("%d %b, %Y"))

    userGuess = get_input(prompt = "What is your guess?\n",
                        cast = int,
                        condition = lambda x: -1 < x < 7,
                        errorMessage = "Please enter a valid day number (0 being sunday,1 monday, 2 tuesday etc.)")

# Adding +1 due to the format difference in .weekday function monday being a 0 instead of sunday as in the original 
# doomsday algorithm and making sure of the exception: answer-0 (sunday) is equal to the program's definiton of sunday-6
    if userGuess == pseudoRandomDate.weekday() + 1 or (userGuess == 0 and pseudoRandomDate.weekday() == 6):
       print("You are correct.")
       userScore += 1
    else:
        print("Wrong answer, the correct one was", pseudoRandomDate.weekday())
    x += 1

print("You were", userScore / questionAmount * 100, "% accurate. You got", userScore,"out of", questionAmount, "questions right.")
exit = input("Press enter to exit")
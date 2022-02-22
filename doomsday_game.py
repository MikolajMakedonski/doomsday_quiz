import datetime
import random
user_score = 0

def get_input(prompt="",cast=None, condition=None, errorMessage=None):
    while True:
        try:
            response = cast(input(prompt))
            assert condition is None or condition(response)
            return response
        except:
            print(errorMessage)

print("Hi, welcome to The doomsday calculation game!")
difficulty_level = get_input(prompt="Please choose the number associated with the desired difficulty level:\n1. Begginner (1900-2099)\n2. Intermediate (1800-2199)\n3. Hard (1-9999)\n",
                        cast=int,
                        condition=lambda y: 4>y>0,
                        errorMessage=("Please enter the difficulty 1-3."))
question_amount = get_input(prompt="How many times do you want to guess?\n",
                        cast=int,
                        condition=lambda y: y>0,
                        errorMessage="Please choose a valid number of questions desired.")

if difficulty_level == 1:
    start_date = datetime.date(1900,1,1)
    end_date = datetime.date(2099,12,31)
elif difficulty_level == 2:
    start_date = datetime.date(1800,1,1)
    end_date = datetime.date(2199,12,31)
elif difficulty_level == 3:
    start_date = datetime.date(1,1,1)
    end_date = datetime.date(9999,12,31)

dates_span = end_date - start_date
days_between_dates = dates_span.days

print("Rule: For a random date, you answer what day of the week that is:\n0-Sunday 1-Monday 2-Tuesday 3-Wednesday 4-Thursday 5-Friday 6-Saturday")
for x in range(question_amount):
    randomized_number_of_days = random.randrange(0,days_between_dates)
    psuedo_random_date = start_date + datetime.timedelta(days = randomized_number_of_days)
    print("Your date to guess is",psuedo_random_date.strftime("%d %b, %Y"))

    user_guess = get_input(prompt="What is your guess?\n",
                        cast=int,
                        condition= lambda x:-1<x<7,
                        errorMessage="Please enter a valid day number (0 being sunday,1 monday, 2 tuesday etc.)")

# Adding +1 due to the format difference in .weekday function monday being a 0 instead of sunday as in the original doomsday algorithm and making sure of the exception: answer-0 (sunday) is equal to the program's definiton of sunday-6
    if user_guess == psuedo_random_date.weekday()+1 or (user_guess==0 and psuedo_random_date.weekday()==6):
       print("You are correct.")
       user_score += 1
    else:
        print("Wrong answer, the correct one was",psuedo_random_date.weekday())
    x+=1

print("You were",user_score/question_amount*100,"% accurate. You got",user_score,"out of",question_amount,"questions right.")
exit = input("Press enter to exit")

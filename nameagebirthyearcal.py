import datetime
name = input('What is your name?\n')
print('Hi, %s.' %name + 'How old are you?')
age_years = int(input()) 
print('Thank you for telling me your age!')
now = datetime.datetime.now()
current_year = now.year
BirthYear = current_year - age_years
print(f"So {name}, you are {age_years} years old. This means you were born in {BirthYear}.")
confirm = input("Unless, your birthday has passed? Has it?\nAnswer with yes or no: ")
if confirm.strip().lower() == "yes":
    print(f"Good, enjoy the {BirthYear} life!")
else:
    print(f"Sorry to hear you were actually born in {BirthYear - 1}")


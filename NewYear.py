import datetime

def bye_last_year():
    print("Bye", currentYear - 1)

def begin_fireworks():
    print("Booom")

def happy_new_year():
    print("Welcome", newYear)

now = datetime.datetime.now()
currentYear = now.year
newYear = 2022

if(currentYear == newYear):

    bye_last_year()
    begin_fireworks()
    happy_new_year()
print("Welcome, were guessing how much time you have on earth \nWanna play? ")
ans = input("Y/N\n")
if ans == ("y"):
    # Dont change code below
    age = int(input("How old are you rm?\n"))
    # Dont change code below
    a = 90 - age
    if a == 0:
        print("You're dead bro")
    else :
        print("good job staying alive buttttt")
        # a = 90 - age
        days = a * 365
        weeks = a * 52
        months = a * 12
        message = f"You are {age} years old, you have {days} days left, also {weeks} weeks left and finally...... {months} months left good luck with your life"

        print(message)
else :
    print("Nigga you suck")
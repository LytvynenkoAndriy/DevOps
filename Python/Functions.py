# Defining the function
def add(arg1, arg2):
    total = arg1 + arg2
    return total

print(add(2,3)) 

def adder(arg1, arg2):
    total = arg1 + arg2
    print(total) # If you have no RETURN - hidden return will display as None

adder(10, 50)
print(adder(10,40))

def summ(arg):
    x = 0
    for i in arg:
        x = x + i
    return x

print(summ([1, 2, 3, 4, 5]))
# print(out)

# summ([10, 20], [30, 40]) # in function specified only 1 argument but 2 were given

# Default argument
def greetings(MSG="Morning"):
    print(f"Good {MSG}")
    print("Welcome to function.")

greetings("")
greetings("Evening")

# Keyword arguments
def vac_feedback(vac, efficacy):
    print(f"{vac} vaccine is having {efficacy} % efficacy")
    if (efficacy > 50) and (efficacy <= 75):
        print ("Seems not so effective, needs more trials")
    elif (efficacy > 75) and (efficacy < 90):
        print ("Can consider this vaccine")
    elif (efficacy >= 90):
        print ("Sure, will take the shot.")
    else:
        print ("Need many more trials")

vac_feedback ("Pfizer", 95)
vac_feedback ("Unknown", 45)
vac_feedback (efficacy=34, vac="Unknown")

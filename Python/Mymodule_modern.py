import random

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

def order_food(min_order, *args):
    print(f"You have ordered: {min_order}")
    for item in args:
        print(f"You have ordered: {item}")
    print("Your food will be delivered in 30 minutes")
    print("Enjoy your party")

import random
def time_activity(*args, **kwargs):
    """
    Input: Multiple values for minutes, key=value pair activity
    Output: Return sum of minutes + random minute spect on a random activity
    """
 #   print(args)
 #   print(kwargs)
    min = sum(args) + random.randint(0, 60)
 #   print(min)
    choice = random.choice(list(kwargs.keys()))
 #   print(choice)
    print(f"You have to spend {min} minutes for {kwargs[choice]}")
























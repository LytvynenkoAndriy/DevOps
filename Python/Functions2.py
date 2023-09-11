#Variable Length Arguments *args (Non keyword arguments)

def order_food(min_order, *args):
    print(f"You have ordered: {min_order}")
    for item in args:
        print(f"You have ordered: {item}")
    print("Your food will be delivered in 30 minutes")
    print("Enjoy your party")

order_food("Salad", "Pizza", "Biryani", "Soup")

#Variable Length Arguments *kwargs (Keyword arguments)

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

time_activity(10,20,10, hobby="Dance", sport="Boxing", fun="Driving", work="DevOps")
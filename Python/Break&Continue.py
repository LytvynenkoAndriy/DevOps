# Break Statement
for i in "DevOps":
    print (i)
    if i == "O":
        print("Found my data.")
        break

print("Out of loop")

# Continue statement

for i in "DevOps":
    if i == "O":
        print("Found my data!")
        continue
    print(f"Value of i is {i}")

print("Out of loop")

# Second statement
import random
VACCINES = ["Moderna", "Pfizer", "Sputnik", "AstraZeneka", "Covaxine", "CoronaVac"]

random.shuffle(VACCINES)
print(VACCINES)

LUCKY = random.choice(VACCINES)
print(LUCKY)

for vac in VACCINES:
    print(f"*****Testing Vaccine {vac}")
    if vac == LUCKY:
        print("#################################")
        print(f"{LUCKY} vaccine, test successful")
        print("#################################")
        print("")
        break
    print("###########################")
    print("Test failed")
    print("###########################")
    print("")

import random
VACCINES = ["Moderna", "Pfizer", "Sputnik", "AstraZeneka", "Covaxine", "CoronaVac"]

random.shuffle(VACCINES)
print(VACCINES)

LUCKY = random.choice(VACCINES)
print(LUCKY)

for vac in VACCINES:
    print(f"*****Testing Vaccine {vac}")
    if vac == LUCKY:
        print("#################################")
        print(f"{LUCKY} vaccine, test successful")
        print("#################################")
        print("")
        continue
    print("###########################")
    print("Test failed")
    print("###########################")
    print("")

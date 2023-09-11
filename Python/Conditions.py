# IF Condition
x = 21

if (x < 30):
    print("Inside IF block")
    print("x is less than 30")

print("Rest of the code.")

# IF/ELSE Condition
x = 31

if (x < 30):
    print("Inside IF block")
    print("x is less than 30")
else:
    print("Inside Else block")
    print("x is greater than 30")

# If/Elif/Else Condition
x = 40

if (x > 40):
    print("Inside IF block")
    print("x is greater than 40")
elif (x == 40):
    print("Inside Elif block")
    print("x is equal to 40")
else:
    print ("x is less than 40")


print("This IT organization has various skill sets.")
print("Find out your match.")
print("Enter Capitalized Values.")

usr_skill = input("Enter your desired skill: ")

DevOps = ["Jenkins", "Ansible", "Bash", "Puppet", "Docker", "Kubernetes", "Terraform"]
Development = ("Nodejs", "Angularjs", "Java", ".net", "Python")
cntr_emp1 = {"Name":"Santa", "Skill":"Blockchain", "Code":1024}
cntr_emp2 = {"Name":"Rocky", "Skill":"AI", "Code":2042}

if usr_skill in DevOps:
    print(f"We have {usr_skill} in DevOps Team.")
elif usr_skill in Development:
    print(f"We have {usr_skill} in Development Team.")
elif (usr_skill in cntr_emp1.values()) or (usr_skill in cntr_emp2.values()):
    print(f"We have contract employees with {usr_skill} skill.")
else:
    print("Skill not found.")
    print("Please check if you have entered value in capitalize or check the spelling.")

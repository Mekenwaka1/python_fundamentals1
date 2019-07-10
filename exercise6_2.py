prompt = "Would you like to walk or run?"
number = 0
energy = 0

while (True):
    print(prompt)
    my_string = str(input())

    if (my_string == "go home"):
        break
    
    elif (my_string == "walk"):
        number += 1
        energy += 1
        print("Distance from home is {}km.".format(number))
        
    elif my_string == "run" and energy > 0:
        number += 5
        energy -= 1 
        print("Distance from home is {}km.".format(number))
    
    elif my_string == "run" and energy == 0:
        print("You do not have energy to run") 

    else:
        print("Command does not exist.")
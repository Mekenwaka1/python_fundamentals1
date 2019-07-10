prompt = "Would you like to walk or run?"
number = 0

while (True):
    print(prompt)
    my_string = str(input())

    if (my_string == "go home"):
        break
    
    elif (my_string == "walk"):
        number += 1
        print("Distance from home is {}km.".format(number))
        
    elif my_string == "run":
        number += 5 
        print("Distance from home is {}km.".format(number))
    else:
        print("Command does not exist.")
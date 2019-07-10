prompt = "Would you like to walk or run?"
number = 0

while (True):
    print(prompt)
    string = str(input())
    
    if (string == "walk"):
        number += 1
        print("Distance from home is {}km.".format(number))
        
    elif string == "run":
        number += 5 
        print("Distance from home is {}km.".format(number))
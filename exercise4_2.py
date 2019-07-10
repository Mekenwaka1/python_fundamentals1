age = int(input())
if age > 25: 
    difference = age - 25
    print("Difference is {} years apart.".format(difference))
else:
    difference = 25 - age
    print("Difference is {} years apart.".format(difference))
if age > 105:
    print("I'm not sure I believe you")  
# *args is a tuple that allows a function to have many different arugument to it

def add(*args):
    sum = 0
    #if you need to change stuff once in the tuple you can change it ot a list 
    args = list(args)
    args[0] = 25
    #this lets us change whats in possition 1 from 4 to 25, we cannot change a tuple but can change the tuple to a list then change the list  

    for i in args:
        sum += i
    return sum


print(add(4,5,6,10))

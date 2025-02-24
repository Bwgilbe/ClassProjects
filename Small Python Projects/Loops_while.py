#while loop = a statement that will continuously execute it's block of code while the statement is true 

#while 1== 1: 
    #print("Help, I'm stuck in a loop")
#this wont let the program stop, this keeps repeating forever

name = ""
while len(name) == 0: 
    name = input("Enter your name: ")
print("Hello "+name)

#another way of writting this code
name = None
while not name:
    name = input("Enter your name: ")
print("Hello "+name)
#This is for break 
while True: 
    name = input("Enter your name: ")
    if name != "":
        break
    
phone_number = "317-313-1267"

for i in phone_number:
    if i == "-":
        continue
    print(i,end="")
    

for i in range(1,20+1): 
    if i ==13: 
        pass 
    else: 
        print(i)
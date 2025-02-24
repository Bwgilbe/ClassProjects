temp = int(input("What is the temperature outside?: "))

if temp >= 60 and temp <= 90: 
    print("The tenperature is good outside!!")
    print("Goo outside!!")
#this is the use of and, both statements have to be true for this to run. 
elif temp < 0 or temp > 30: 
    print("The temperature is bad today")
    print("Stay indoors!!")
# this is the use of or, only one of the conditions must be met for this to run. 


#this is the use of not 
if not(temp >= 60 and temp <= 90): 
    print("The tenperature is good outside!!")
    print("Goo outside!!")
    print("The temperature is bad today")
    print("Stay indoors!!")
 
elif not(temp < 0 or temp > 30): 
    print("The tenperature is good outside!!")
    print("Goo outside!!")

#not will make whats true false, and whats false true. inverse the problem 
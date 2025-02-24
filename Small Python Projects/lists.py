# list or arrays  are used to store multiple items in one variable 
# list are shown by using 

food = ["pizza","hamburger","hotdog","spagetti","pudding"]

print(food)

food[0] = "sushi"
#this changes what 0 is, from pizza to sushi
print(food[0])

food.append("ice cream")
#this adds ice cream to the list ad the end 

food.remove("hotdog")
#this removes hotdog from this list 

food.pop()
#this removes the last item in the list, in this case its ice cream from appending it onto the list 

food.sort()
# this will sort the list in alphabetical order

# food.clear() 
# this clears the items in the list 
for i in food:
    print(i)
    
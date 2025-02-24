
utensils = {"fork","spoon","knife","knife","knife","knife","knife"}
dishes = {"Bowl","plate","cup","knife"}


utensils.add("napkin")
#-this will add items to set, this will still be in any order 

#utensils.remove("fork")
#-this will remove item from the set, fork will be removed from the set 

#utensils.clear()
#- this will clear the set 

for i in utensils:
    print(i)
    
print()
# adding our dishes to utensils

#dishes.update(utensils)
# you can also do it by utensils.update(dishes)
# in the for put in utensils
for i in dishes:
    print(i)
    
print()

dinner_table = utensils.union(dishes)

for i in dinner_table:
    print(i)
    
    
    
#this will compare the difference from utinsils 
print(dishes.difference(utensils))
#this shows what they have in common
print(dishes.intersection(utensils))
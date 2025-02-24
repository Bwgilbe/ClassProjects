capitals = {'USA':'Washington DC', 'India':'New Dehlia','China':'Beijing','Russia':'Moscow'}

#capitals.update({'Germany':'Berlin'})
#- this updates the list and lets you gain a new item to the collection of values 
#- you can also do it with existing keys 

capitals.pop('China')
#-this will remove china from the list 

#to print different  values 
print(capitals['Russia']) #= Moscow
#- cant add new things with this method 

#Get method 
print(capitals.get('Germany'))
#-this allows you to check to see if there are in your dictionary without having the program fail 
#
print(capitals.keys())
#-this will print all of the keys 

print(capitals.values())
#-this will print all of the values 

print(capitals.items())
#-this will print the keys and items together 

for key,value in capitals.items(): 
  print(key,value)
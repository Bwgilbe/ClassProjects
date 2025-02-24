#tuples are collection of ordered and unchangle items 
# used to group related data together 
student = ("Bro",21,"Male")

print(student.count("Bro"))

print(student.index("Male"))

for x in student:
  print(x)


if "Brp" in student:
  print("Bro is here!")
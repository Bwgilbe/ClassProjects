from OOP_Car import Car

Car_1 = Car("Chevy","Silverado",2011,"Blue-Grey")

Car_2 = Car("Ford","Mustang",1997,"White")

print(Car_1.make)
print(Car_1.color)
print(Car_1.model)
print(Car_1.year)

Car_1.drive()
Car_2.stop()
Car_1.Turn_Left()

print(Car_1.wheels)
#this prints the default 4 wheels 

Car_1.wheels = 6

print(Car_1.wheels)
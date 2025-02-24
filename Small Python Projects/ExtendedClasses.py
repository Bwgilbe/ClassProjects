class Animal:
    #this is the parent class, this will pass anything it has to the child class 
    alive = True 
    
    
    def eat(self):
        print("This animal is eating")
        
    def sleep(self):
        
        print ("The animal is sleeping")
        
class Rabbit(Animal):
    pass

class Fish(Animal):
    pass

class Hawk(Animal):
    pass

rabbit = Rabbit()

fish = Fish()
hawk = Hawk()


print(rabbit.alive)
print(fish.eat)
print(hawk.sleep)

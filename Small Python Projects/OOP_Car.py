class Car:
    
    # we can make default varilables that will apply to all instances of the class, but it can also be changed 
    
    wheels = 4 
       
    # you will always need self, to preform the other actions, this does not count for what you have to pass in. you only need to pass in the other arguments in this case 
    # make, model year and color total of 4 atrabutes not 5. 
    def  __init__(self, make, model, year,color):
        
        self.make = make 
        self.model = model
        self.year = year 
        self.color = color 
    
    def drive(self):
        print("This",self.model,"is Driving")
        
    def stop(self):
        print("This",self.model,"has stopped")

    def Turn_Left(self):
        print("This",self.model,"has turned Left")
        
    def Turn_Right(self):
        print("This",self.model,"has turned Right")
import time
#for loop - a statement that will execute it's block of code 
#           a limited number of times 

# i = index 

for i in range(10):
    print(i)
    
                # 50 = the starting number, this includes 50  
                    # 100 = the ending number, this excludes 100, we are adding a 1 to include that number     
                      # 2 = the amount of times we are skipping over numbers, 50, 52, 54, 56 ...            
for i in range(50,100+1,2):
  print(i)
  
for i in "Brodie Gilbert": 
    print(i)
    
#we are going to make a count down timer
for sec in range(10,0,-1):
    print(sec)
    time.sleep(1)
print("Happy New YEAR")
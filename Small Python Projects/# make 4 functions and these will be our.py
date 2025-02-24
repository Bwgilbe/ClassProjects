# make 4 functions and these will be our fram works for this game 

def new_game():
    
    guesses = []
    
    correct_guesses = 0 
    question_num = 1
    
    for key in questions:
        print("--------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter your answer (A,B,C,D): ").upper()
        guesses.append(guess)
        #this will place the answer from guess into the list guesses
        
        
        # the += is what allows us to score more then 1 point, this allows us to keep a tally
        correct_guesses += check_answers(questions.get(key),guess)
        # you can assign a variable to a function, this is giving out if the person made a right answer and either increases or decreases thier score 
        
        # questions is the answer  and guess is the guess of the current question
        question_num +=1
    display_score(correct_guesses,guesses)

def check_answers(answer,guess): #note that these are variables I made, the do not have to be the same as im putting in. they a re placeholders for outside the functions, variables inside the function
    if answer == guess:
        print("CORRECT ANSWER!!!!")
        return 1 
    else:
        print("WRONG ;(")
        return 0
    
    

def display_score(correct_guessess,guessess):
    print("----------------------")
    print("RESULTS")
    print("----------------------")
    print("Ansers: ", end="")
    for i in questions:
        print(questions.get(i),end=" ")
        print()
        
    print("Guesses: ",end="")
    for i in guessess:
        print(i,end=" ")
    print()
    
    score = int((correct_guessess/len(questions))*100)
    
    print("Your score is:",score,"%")

def play_again():
    response = input("Do you want to play again? (Y or N)").upper()
    
    if response == "Y":
        return True
    else: 
        return False

questions = {"Who created Python?: ": "A",
             "What year was Python created?: ":"B",
             "Python is tributed to which comedy group?: ": "C",
             "Is the Earth round?: ": "A"
             }

# we are making a list of lists, each list in order will have the answers of the questions, with doing lists we dont have to do that all that matters is that all the 
# answers are grouped together

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuck"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A.True", "B.False", "C.Maybe", "D.None of the above"]]

new_game()

while play_again():
    new_game()
print("See you next time!")
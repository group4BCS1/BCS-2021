try:
    score = float(input('Enter Score:\n ')) #Getting the user's score input
    def computegrade(score):            #Defining the function
        if score > 0.0 and score < 1.0:  #Setting the range for the valid user input
            if score >= 0.9:
                print('A')         #Printing the grade according to the score
            elif score >= 0.8:
                print('B')
            elif score >= 0.7:
                print('C')
            elif score >= 0.6:
                print('D')
            else:
                print('F')
        else:
            print('Bad Score')
except:
    print('Bad Score')
    
computegrade(score) #Calling the function
                    
    
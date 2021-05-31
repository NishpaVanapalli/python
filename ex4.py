##import random
##people  = []
##for x in range(0,8):
##    person = input("Type the name of a person: ")
##    people.append(person)
##index = random.randint(0,7)
##random_person = people[index]
##print("Picking a random person: ", random_person)
##############################################################


##import random
##colors = ["white", "black", "red", "green", "blue", "yellow", "purple", "grey"]
##while True:
##    color = colors[random.randint(0,len(colors)-1)]
##    guess = input("I'm thinking about a color,  canyou guess it: ")
##    while True:
##        if (color == guess):
##            break
##        else:
##            guess = input("Nope. Try again: ")
##    print("You guessed it! I was thinking about ", color)
##    play_again = input("Let's play again? Type 'no' to quit. ")
##
##    if play_again.lower() == "no":
##        break
##print("It was fun, thanks for playing!")
####################################################################            


##data_valid = False
##while data_valid == False:
##    grade1 = float( input("Type the grade of the first test: ") )
##    if grade1 < 0 or grade1 > 10:
##        print("Grade should be between 0 and 10 ")
##        continue
##    else:
##        data_valid = True
##
##data_valid = False
##while data_valid == False:
##    grade2 = float( input("Type the grade of the second test: ") )
##    if grade2 < 0 or grade2 > 10:
##        print("Grade should be between 0 and 10 ")
##        continue
##    else:
##        data_valid = True
##
##data_valid = False
##while data_valid == False:
##    total_classes = int( input("Type the total number of classes: ") )
##    if total_classes <= 0:
##        print("The number of classes can't be zero or less")
##        continue
##    else:
##        data_valid = True
##
##
##data_valid = False
##while data_valid == False:
##    absences = int( input("Type the number of absences: ") )
##    if absences < 0 or absences > total_classes:
##        print("The number of absences can't be less than zero or greater than the number of total classes.")
##        continue
##    else:
##        data_valid = True
##        
##avg_grade = (grade1 + grade2) / 2
##attendance = (total_classes - absences) / total_classes
##
##print("Average grade: ", round(avg_grade,2))
##print("Attendance rate: ", str(round((attendance*100),2))+ "%")
##if(avg_grade >= 6 and attendance >= 0.8):
##    print("The student has been approved. ")
##elif(avg_grade < 6 and attendance < 0.8):
##     print("The student has failed due to an average grade lower than 6.0 and an attendance rate lower than 80%. ")
##elif(attendance >= 0.8):
##    print("The student has failed due to an average grade lower than 6.0. ")
##else:
##    print("The student has failed due to an attendance rate lower than 80%. ") 
##########################################################################################



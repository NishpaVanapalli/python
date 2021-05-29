##months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
##birthday = input("Type your birthday in the format DD-MM-YYYY: ")
##
##index = int(birthday[3:5]) - 1
##bd_month = months[index]
##
##print("You were born in ", bd_month)
################################################################


##people = ["John", "Mary", "Peter"]
##user = input("Type ypur name: ")
##people.append(user)
##print("Here's the list : ", people)
####################################################################


##person = {"name" : "John Green", "gender" : "M", "age" : "35", "address" : "109 Penny Lane", "phone" : "7075088482"}
##key = input("What information do you want to know about the person? ").lower()
##result = person.get(key, "That information is not available")
##print(result)
############################################################################


##num1 = float(input("Type the first number: "))
##num2 = float(input("Type the second number: "))
##if(num1 > num2):
##    print(num1 , "is gerater than ", num2)
##elif(num1 == num2):
##    print(num1 , "is equal to ", num2)
##else:
##    print(num1 , "is less than ", num2)
##################################################################


##my_age = 32
##user_age = int(input("Type your age: "))
##if(my_age > user_age):
##    print("You are younger than me")
##elif(my_age < user_age):
##    print("You are older than me")
##else:
##    print("We two have same age")
######################################################################


##grade1 = float( input("Type the grade of the first test: ") )
##grade2 = float( input("Type the grade of the second test: ") )
##absences = int( input("Type the number of absences: ") )
##total_classes = int( input("Type the total number of classes: ") )
##avg_grade = (grade1 + grade2) / 2
##attendance = (total_classes - absences) / total_classes
##
##print("Average grade: ", round(avg_grade,2))
##print("Attendance rate: ", str(round((attendance*100),2))+ "%")
##if(avg_grade >= 6):
##    if(attendance >= 0.8):
##         print("The student has been approved. ")
##    else:
##        print("The student has failed due to an attendance rate lower than 80%. ")
##elif(attendance >= 0.8):
##    print("The student has failed due to an average grade lower than 6.0. ")
##else:
##    print("The student has failed due to an average grade lower than 6.0 and an attendance rate lower than 80%. ")
############################################################################################


##grade1 = float( input("Type the grade of the first test: ") )
##grade2 = float( input("Type the grade of the second test: ") )
##absences = int( input("Type the number of absences: ") )
##total_classes = int( input("Type the total number of classes: ") )
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
##########################################################################
    

##print("This program claculates your body mass index. ")
##weight = float(input("Type your weight in kg (ex: 70.5): "))
##height = float(input("Type your height in meters (ex: 1.70):"))
##
##bmi = weight / (height ** 2)
##print("Your BMI is: ", round(bmi,2))
##if(bmi <+ 18.5):
##    classification = "Under weight"
##elif(bmi > 18.5 and bmi <= 24.9):
##    classification = "Normal weight"
##elif(bmi > 24.9 and bmi <= 29.9):
##    classification = "Over weight"
##else:
##    classification = "Obesity"
##print("The classification of your BMI is: ", classification)
############################################################################



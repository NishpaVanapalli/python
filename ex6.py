##def say_hello():
##    print("Hello!")
##say_hello()
##say_hello()
##say_hello()
####################################################


##def say_hello(person):
##    print("Hello " + person + "how are you doing? ")
##say_hello("Mary")
##say_hello("Paul")
##say_hello("Kate")
####################################################


##def say_hello(person1, person2="The director"):
##    print("Hello " + person1 + " how are you doing? " + person2 + " is waiting for you.")
##def fahr2celcius(fahr):
##    celcius = (5 * (fahr - 32))/9
##    return celcius
##say_hello("Jane", "Tim")
##print("Celcius: " , round(fahr2celcius(100),2 ) )
##print("Kelvin: " , round(fahr2celcius(100) + 273.5 ,2 ) )
############################################################


##import matplotlib.pyplot as plt
##import time as t
##times = []
##mistakes = 0
##
##print("This program will help you type faster. You will have to type the word 'programming' as fast as you can for five times. ")
##input("Press enter to continue. ")
##while len(times) < 5:
##    start = t.time()
##    word = input("Type the word: ")
##    end = t.time()
##    time_elapsed = end - start
##
##    times.append(time_elapsed)
##
##    if(word.lower() != "programming"):
##        mistakes += 1
##
##print("You made " + str(mistakes) + " mistake(s). ")
##print("Now let's see your evolution")
##t.sleep(3)
##
##x = [1,2,3,4,5]
##y = times
##plt.plot(x,y)
##legend = ["1", "2", "3" , "4", "5"]
##plt.xticks(x,legend)
##plt.xlabel("Attempts")
##plt.ylabel("Time in seconds")
##plt.title("Your typing evolution")
##plt.show()
########################################################


 

##from math import *
##a = 2.13
##b = 3.7777
##c = -3.12
##print(int(c)==floor(b))


##from math import factorial
##print(math.factorial(5))


###mod1
##def change(a):
##    b=[x*2 for x in a]
##    print(b)
###mod2
##def change(a):
##    b=[x*x for x in a]
##    print(b)
##from mod1 import change
##from mod2 import change
###main
##s=[1,2,3]
##change(s)


##import math
##a=math.floor(3.4)
##b=math.ceil(2.3)
##c=math.trunc(3.1)
##print(a==c and b==c)


##import math
##a=math.floor(3.4)
##b=math.ceil(2.3)
##print(a==b)


##def foo():
##    try:
##        return 1
##    finally:
##        return 2
##k = foo()
##print(k)


##def foo():
##    try:
##        print(1,end=" ")
##    finally:
##        print(2)
##foo()


##a=10
##try:
##  s=a+b
##  s=a/0
##except ZeroDivisionError:
##  print("ZeroDivisionError")
##except NameError:
##  print("Name Error")
##else:
##  print("No Error")
  


##def f(x):
##  try:
##    x = x / x
##  except:
##    print("a",end='')
##  else:
##    print("b",end='')
##  finally:
##    print("c",end='')
##f(1)
##f(0)


##try:
##  if('1'==1):
##    a=10
##  else:
##    a=20
##except ZeroDivisionError:
##  print("ZeroDivisionError")
##except NameError:
##  print("Name Error")
##else:
##  print("No Error")


##try:
##    print('try')
##except ValueError:
##    print('ValueError')
##finally:
##    print('finally')


##data = 50
##try:
##    data = data/10
##except ZeroDivisionError:
##    print('Cannot divide by 0 ', end = '')
##finally:
##    print('TechnicalHub ', end = '')
##else:
##    print('Division successful ', end = '') 


##data = 50
##try:
##    data = data/0
##except ZeroDivisionError:
##    print('Cannot divide by 0 ', end = '') 
##else:
##    print('Division successful ', end = '')
##finally:
##    print('Technical Hub ', end = '') 


##try:
##    # Do something
##except:
##    # Do something
##else:
##    # Do something



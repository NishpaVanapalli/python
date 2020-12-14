##def f(x):
##    if x == 0:
##        return 0
##    return x + f(x - 1)
##print(f(3))


##def func1(a):
##    return a ** a
##def func2(a):
##    return func1(a)*func1(a)
##print(func2(2))



##def func(a,b):
##    return a ** a
##print(func(2))


##def fun(x):
##    global y
##    y = x * x
##    return y
##
##fun(2)
##print(y)


##def I():
##    s = 'abcdef'
##    for c in s[::2]:
##        return c
##for x in I():
##    print(x,end='')


##def fun(x):
##    x += 1
##    return x
##x = 2
##x = fun(x+1)
##print(x)



##def func(a,b):
##    return b ** a
##print(func(b=2,a=2))


##def list(L):
##    del L[3]
##    return L
##
##L =  ['Mary', 'had', 'a', 'little', 'lamb']
##L[3] = 'ram'
##
##print(list(L))


##def func1(a):
##    return None
##def func2(a):
##    return func1(a)*func1(a)
##print(func2(2))



##def fun(inp=2,out=3):
##    return inp * out
##print(fun(out=2))


##def fun(x):
##    if x % 2 == 0:
##        return 1
##    else:
##        return 2
##print(fun(fun(2)))


##def fun(x,y):
##    if x == y:
##        return x
##    else:
##        return fun(x,y-1)
##print(fun(0,3))


##list =  [x*x for x in range(5)]
##def fun(L):
##    del L[L[2]]
##    return L
##print(fun(list))


##def I(n):
##    s = '+'
##    for i in range(n):
##        s += s
##        return s
##
##for x in I(2):
##    print(x,end='')


##def fun(x):
##    if x % 2 == 0:
##        return 1
##    else:
##        return   0
##print(fun(fun(2)) + 1)


##def I(n):
##    s = '+'
##    for i in range(n):
##        s += s
##    return s
##
##for x in I(2):
##    print(x,end='')


##def fun(inp=2,out=3):
##    return inp * out
##print(fun(out=2))


##def Odd(a, b):
##    if (a & 1 and b &1):
##        print ("Both are Odd")
##    elif(a&1):
##        print ("%d is Odd"%(a))
##    elif(b&1):
##        print ("%d is Odd"%(b))
##Odd(3, 4)


##def maximum(x, y):
##    if x > y:
##        return x
##    elif x == y:
##        return 'The numbers are equal'
##    else:
##        return y
## 
##print(maximum(2, 3))


##def cube(x):
##    return x * x * x      
##x = cube(3)    
##print (x)


##def C2F(c):
##    return c * 9/5 + 32 
##print(C2F(100),)
##print(C2F(0))


##def power(x=1, y=2):
##    r = 1
##    for i in range(y):
##        r = r * x
##    return r
##print (power())
##print (power(3, 3))


##def a(b):
##    b = b.append(5)
##c = [1, 2, 3, 4]
##a(c)
##print(len(c))


##def printMax(a, b):
##    if a > b:
##        print(a, 'is maximum')
##    elif a == b:
##        print(a, 'is equal to', b)
##    else:
##        print(b, 'is maximum')
##printMax(3, 4)


##def fun(x,y,z):
##    return x+2*y+3*z
##print(fun(0,z=1,y=3))


##y = 6
##z = lambda x: x * y
##print(z(8))



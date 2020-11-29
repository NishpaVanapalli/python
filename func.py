##x=int(input('enter a number '))
##y=int(input('enter a number '))
##def add (x,y):
##    print('x', x)
##    print('y', y)
##    c=x+y
##    print(c)
##add(x,y)



##def human(name,age):
##    print(name)
##    print(age+5)
##human('nishpa',18)



##y=(100,200,300,400,500,600,700,800,900)   
##for i in y:
##    print(i)



##def add(*y):
##    c=0
##    for i in y:
##        c+=i
##    print(c)
##add(10,20,30,40,50)



##def add(x,y):
##    c=x+y
##    return c
##result=add(10,20)
##print(result)
##
##def sub( ):
##    a= result-1
##    print(a)
##sub( )



##n=int(input('enter a number '))
##def add( ):
##    print(n,'in')
##add( )
##print(n,'out')



##number is even or odd##
##n= int(input('enter a number '))
##def is_even_odd(n):
##    if n%2==0:
##        print('even')
##    else:
##        print('odd')
##is_even_odd(n)
    


##number is prime or not##
##n=int(input('enter a number '))
##def is_prime(n):
##    count=0
##    for i in range(1,n+1):
##        if n%i==0:
##            count+=1
##    if count==2:
##        return True
##    else:
##        return False
##print(is_prime(n))

##def main( ):       ##
##    if is_prime(7):##
##        print('hai')##



##nearest prime##
##n= int(input('enter a number '))
##from math import sqrt
##def is_prime(n):
##    for i in range(n-1,1,-1):
##            if n%i==0:
##                return False
##    return True
####print(is_prime(7))   
##
##def left_prime(n):
##    i=n-1
##    while True:
##        if is_prime(i):
##            return i
##        i-=1
####print(left_prime(9))
##
##def right_prime(n):
##    j=n+1
##    while True:
##        if is_prime(j):
##            return j
##        j+=1
####print(right_prime(9))
##     
##def nearest_prime(n):
##    if is_prime(n):
##        return n
##    else:
##        x= right_prime(n)
##        y= left_prime(n)
##        if abs(n-x)>abs(n-y):
##            return y
##        elif abs(n-x)<abs(n-y):
##            return x
##        else:
##            return x,y
##print(nearest_prime(n))



##pattern printing using functions##
##n= int(input('enter a number '))
##def pattern(n):
##    for i in range(1,n+1):
##        for k in range(n,i,-1):
##            print(' ',end=' ')
##        for j in range(1,i+1):
##            print('*',end=' ')
##        print( )
##pattern(n)
##pattern(n)
##pattern(n)



##add,sub,mul,div##
##a= int(input('enter a number '))
##b= int(input('enter a number '))
##def add(a,b):
##    return a+b
##
##def sub(a,b):
##    return a-b
##
##def mul(a,b):
##    return a*b
##
##def div(a,b):
##    return a//b
##
##def prog( ):
##        print(add(a,b))
##        print(sub(a,b))
##        print(mul(a,b))
##        print(div(a,b))

##prog( )

##n= int(input())
##m= int(input())
##print(n+m)



##add,sub.....user input##
##a= int(input('enter a number '))
##b= int(input('enter a number '))
##user= int(input('1/2/3/4:--  '))
##def add(a,b):
##    return a+b
##
##def sub(a,b):
##    return a-b
##
##def mul(a,b):
##    return a*b
##
##def div(a,b):
##    return a//b
##
##def prog( ):
##    if user==1:
##        print(add(a,b))
##    elif user==2:
##        print(sub(a,b))
##    elif user==3:
##        print(mul(a,b))
##    elif user==4:
##        print(div(a,b))
##    else:
##        print('invalid choice')
##prog( )



##def add(a,b):
##    return a+b
##def sub(a,b):
##    return a-b
##def mul(a,b):
##    return a*b
##def div(a,b):
##    return a%b



##prime number using functions##
##n= int(input('enter a number '))
##def prime(n):
##    for i in range(2,n):
##        if n%i==0:
##            return False
##    else:
##        return True



##hollow square##
##def patt(n):
##    for i in range(1,n+1):
##        for j in range(1,n+1):
##            if i==1 or i==n or j==1 or j==n:
##                print('#',end=' ')
##            else:
##                print('  ',end=' ')
##        print( )
##n= int(input('enter a number '))
##patt(n)



##hollow square design##
##def patt(n):
##    for i in range(1,n+1):
##        for k in range(n,i,-1):
##            print(' ', end=' ')
##        for j in range(1,n+1):
##            if i==1 or i==n or j==1 or j==n:
##                print('#',end=' ')
##            else:
##                print('  ',end=' ')
##        print( )
##n= int(input('enter a number '))
##patt(n)



##ABCDEF##
##n=int(input('enter a number '))
##for i in range(0,n):
##    for j in range(65,65+n):
##        print(chr(j),end=' ')
##    print( )



##multiple inputs in a single line##
##a,b,c=map(int,input().split())
##d=a**2+b**2+c**2
##print(d)



##evaluate function##
##a=10
##print(eval('a+2'))
##print(a)


##hollow triangle##
##def holl(n):
##    for i in range(1,n+1):
##        for j in range(n,i,-1):
##            print(' ',end=' ')
##        for k in range(1,i+1):
##            if i==1 or i==n or k==1 or k==i:
##                print(' * ',end=' ')
##            else:
##                print('  ',end='  ')
##        print( )
##n=int(input('enter a number '))
##holl(n)



##A AB ABC....##
##n=int(input('enter a number '))
##for i in range(1,n+1):
##    for j in range(0,i):
##        print(chr(65+j),end=' ')
##    print( )



##1 12 123....##
n=int(input('enter a number '))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    for k in range(n,i,-1):
        print(' *',end=' ')
    print( )

##declaration of class of a variable (int/float/string)## 
##a=input('enter a number')
##b=input('enter a number')
##c=input('enter a number')
##print(type(a),type(b),type(c),a+b,b+c,a+c,a+b+c)





##eligible for campus dirve or not##
##p=float(input('enter your percentage'))
##bl=int(input('enter number of backlogs'))
##if p>=60 and bl==0:
##   print("you are eligible for the campus drive")
##else:
##  print("sorry! you are not eligibe")





##less than or greater than##
##a=int(input("enter a number"))
##b=int(input("enter a number"))
##if a < b:
##  print("a is less than b", a, b)
##else:
##  print("a is greater than b", a, b)




    
##program to declare  the grade obtained using marks##
##m= int(input('enter your marks'))
##if m>=80:
##  print("A grade")
##elif m>=60 and m<80:
##  print("B grade")
##elif m>=40 and m<60:
##  print("C grade")
##else:
##  print("better luck next time")





##increment and decrement operators table using 'for' loop##
##s= int(input('enter a start number '))
##e= int(input('enter a end number '))
##b= int(input('enter a multiplication '))
##if s<=e: 
##    for n in range(s,e+1):
##        print(n,'*',b,'=',n*b)
##else:
##    for n in range(s,e-1,-1):
##        print(n,'*',b,'=',n*b)





##for i in range(2.0,3.0):
##    print(i)





##to print the multiple of even/odd numbers##
##s= int(input('enter a start number '))
##e= int(input('enter a end number '))
##b= int(input('enter a multiplication '))
##for n in range(s,e+1):
##    if n%2==1:
##        print(n,'*',b,'=',n*b)





##1 2 3 4 5 6 7 8 9 10##
##for i in range(11):
##    print(i,end='\t')





##sum of numbers##
##s=0
##for i in range(5,16):
##  s+=i
##    print(s)
##print('therefore the final sum is ',s)





##divisible by 3##
##s=0
##for i in range(5,16):
##    if i%3==0:
##        print(i)




##assignment operator##
##for i in range(1,11,1):
##    i+=2
##    print(i)





##while loop##
##i=10
##while True:
##    i-=1
##    print(i)
    
##    if i==0:
##        break





##i=10
##while not (i<0):
##    print(i)
##    i-=1





##i=0
##while i<30:
##    i+=2
##   if i%3!=0:
##        continue
##    print(i)





#revision#
##s= int(input("enter a starting range "))
##e= int(input("enter a ending range "))
##st= int(input("enter the step count "))
##for i in range(s,e+1,st):
##    print(a,'+',i,'=',i+a)






##i=0
##while i<=1000:
##    print(i)
##    i+=1





##shanmukh login##
##id= "shanmukhsaivanapalli@gmail.com"
##pw= "123456789"

##uid= str(input("enter yout login id "))
##upw= str(input("enter your password "))

##if id==uid and pw==upw:
##    print("login successful! ")
##else:
##    print("oops!! incorrect correct credentials ")





##i=10
##while i>0:
##    i-=1
##    print(i)




##login using for and else##
##id= 'thub@gmail.com'
##pw= '12345'
##
##for i in range(4):
##    uid= str(input('enter your mail id '))
##    upw= str(input('enter your password '))
##    if id==uid and pw==upw:
##        print('login successful')
##        break
##    else:
##        print('wrong credentials')
##
##else:
##    print('account blocked')
##
##print('all are done')

 



##prime number or not##
##n= int(input('enter a number '))
##count= 0
##for i in range(1,n+1):
##    if n%i==0:
##        count+=1
##if count==2:
##    print(n,' is a prime number')
##else:
##    print(n,' is not a prime number')





##prime or not##
##n= int(input('enter a number '))
##for i in range(2,n):
##    if n%i==0:
##        print(n,' is not a prime number')
##        break
##else:
##    print(n,' is a prime number')





##prime or not using while loop##
##n= int(input('enter a number '))
##i=1
##count=0
##
##while i<=n:
##    if n%i==0:
##        count+=1
##    i+=1
##        
##if count==2:
##    print(n,' is a prime number')
##else:
##    print(n,' is not a prime number')





##prime numbers in a group of numbers##
##s= int(input('enter starting range '))
##e= int(input('enter ending range '))
##for j in range(s,e+1):
##    for i in range(2,j):
##        if j%i==0:
##           # print(j,' is not a prime number')
##            break
##    else:
##        print(j,' is a prime number')
            
    



##finding previous prime number to the given number##
##s= int(input('enter starting range '))
##for j in range(s-1,1,-1):
##    for i in range(2,j):
##        if j%i==0:
##            #print(j,' is not a prime number')
##            break
##    else:
##        print(j,' is the prime number before ',s)
##        break





##finding next prime number to the given number##
##s=int(input('enter a number '))
##a=s
##
##while a:
##    for i in range(2,a):
##        if a%i==0:
##            #print(s,' is not a prime number')
##            break
##    else:
##        print(a,' is a prime number after ',s)
##        break
##    a+=1





##nearest prime number##
##s=int(input('enter a number '))
##for j in range(s-1,1,-1):
##    for i in range(2,j):
##        if j%i==0:
##            break
##    else:
##        bp=j
##        print(j)
##        break
##
##a=s
##while True:
##    for i in range(2,a):
##        if a%i==0:
##            break
##    else:
##        ap=a
##        print(a)
##        break
##    a+=1
##
##if abs(s-ap)>abs(s-bp):
##    print('nearest prime number is ',bp)
##elif abs(s-ap)<abs(s-bp):
##    print('nearest prime number is ',ap)
##else:
##    print('nearest prime numbers are ',ap,bp)





##armstrong number##
##n= int(input('enter a number '))
##a=n
##s=0
##
##while n>0:
##    rem= n%10
##    s= s+rem*rem*rem
##    n= n//10
##if a==s:
##    print(a,' is an armstrong number')
##else:
##    print(a,' is not an armstrong number')





##palindrome or not##
##n= int(input('enter a number '))
##a=n
##rev=0
##
##while n>0:
##    rem= n%10
##    rev= rev*10+rem
##    n= n//10
##if a==rev:
##    print(a,' is a palindrome number')
##else:
##    print(a,' is not a palindrome number')





##factorial of a number using while loop##
##n= int(input('enter a number '))
##i=1
##a=n
##fact=1
##
##while i<=n:##n>0
##    fact*= n*i##fact*=n
##    n-=1
##print(fact,' is the factorial of ',a)





##factorial of a number using for loop##
##n= int(input('enter a number '))
##a=n
##fact=1
##
##for i in range(1,n+1):##(n,0,-1)
##    fact*=i
##print(fact,' is the factorial of ',a)
    




##harshed number ##
##n= int(input('enter a number '))
##a=n
##s=0
##
##while n>0:
##    rem= n%10
##    s+=rem
##    n//=10
##print(s,' is the sum of ',a)
##if a%s==0:
##    print(a,' is a harshed number')
##else:
##    print(a,' is not a harshed number')





##fibonocci series using while loop##
##n= int(input('enter a range '))
##a=0
##b=1
##print(a,b,end=" ")
##count=3
##
##while count<=n:
##    s= a+b
##    print(s,end=" ")
##    a=b
##    b=s
##    count+=1





##fibonocci series using for loop##
##n= int(input('enter a range '))
##a=0
##b=1
##print(a,b,end=' ')
##
##for count in range(1,n-1):##(2,n)
##    s= a+b
##    print(s,end=' ')
##    a=b
##    b=s





##previous number of fibnocci series from the given number##
##n= int(input('enter a number '))
##a=0
##b=1
##for i in range(3,n+1):
##    s=a+b
##    a=b
##    b=s
##    if b>=n:
##        print(a)
##        break





##next number of fibnocci series from the given number##
##n= int(input('enter a number '))
##a=0
##b=1
##for i in range(3,n+1):
##    s=a+b
##    a=b
##    b=s
##    if b>=n:
##        print(b)
##        break





##perfect numbers using for loop##
##n= int(input('enter a number '))
##a=n
##s=0
##
##for i in range(1,n):#(1,(n//2)+1)#
##    div=n%i
##    if n%i==0:
##        s+=i
##    else:
##        continue
##    
##if s==a:
##    print(a,' is a perfect number')
##else:
##    print(a,' is not a perfect number')





##perfect numbers using while loop##
##n= int(input('enter a number '))
##a=n
##s=0
##i=1
##
##while i<n:
##    if n%i==0:
##        s+=i
##    i+=1
##       
##if s==a:
##    print(a,' is a perfect number')
##else:
##    print(a,' is not a perfect number')





##pattern printing n*n using for loop##
##n=int(input('enter a number '))
##for i in range(1,n+1):
##    for j in range(1,n+1):
##        print('*',end=' ')
##    print( )





##pattern printing n*n using while loop##
##n=int(input('enter a number '))
##i=1
##while i<=n:
##    j=1
##    while j<=n:
##        print('*',end=' ')
##        j+=1
##    print( )
##    i+=1
    
   



##pattern printing numbers 1*n##
##n= int(input('enter a number '))
##for i in range(1,n+1):        #row
##    for j in range(1,n+1):       #column
##        print(i,end=' ')
##    print( )





##pattern printing i*n using for loop##
##n= int(input('enter a number '))
##for i in range(1,n+1):
##    for j in range(1,i+1):
##        print('*',end=' ')
##    print( )





##pattern printing 1*n using while loop##
##n=int(input('enter a number '))
##i=1
##while i<=n:
##    j=1
##    while j<=i:
##        print('*',end=' ')
##        j+=1
##    print( )
##    i+=1





##pattern printing numbers 1-n##
##n= int(input('enter a number '))    
##for i in range(1,n+1):
##    for j in range(1,i+1):
##        print(j,end=' ')
##    print( )





##pattern printing n*1##
##n=int(input('enter a number '))
##for i in range(1,n+1):
##    for j in range(n,i-1,-1):
##        print('*',end=' ')
##    print( )





##pattern printing design 1*n triangle##
##n=int(input('enter a number '))
##for i in range(1,n+1):
##    for k in range(n,i,-1):
##        print(' ',end=' ')
##    for j in range(1,i+1):
##        print(' * ',end=' ')
##    print( )





##pattern printing design n*n square##
##n=int(input('enter a number '))
##for i in range(1,n+1):
##    for k in range(n,i,-1):
##        print(' ',end=' ')
##    for j in range(1,n+1):
##        print('*',end=' ')
##    print( )

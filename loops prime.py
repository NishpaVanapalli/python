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


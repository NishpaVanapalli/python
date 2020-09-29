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

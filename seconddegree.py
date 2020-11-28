##a=input('enter a number')#dkjvhdjskgh
##b=input('enter a number')#kgbjkbjkdfnbjkDH
##print(type(a),type(b),a,b,a+b)
##
##a=int(a)
##b=int(b)
##print(type(a),type(b),a,b,a+b)
##
##a=float(a)
##b=float(b)
##print(type(a),type(b),a,b,a+b)
##
##

##a=10
##b=20
##if a<15 and b>15:#T and T
##    print(a)
##    print(b)
##
##print('done')

#per>=60   bl=0
##p=float(input('enter percentage'))
##bl=int(input('enter no of backlogs'))
##if p>=60 and bl==0:
##    print('eligible')
##else:
##    print('not eligible')

##a=int(input('enter a marks'))
##b=int(input('enter a marks'))
##if a>b:
##    print('a is topper')
##else:
##    print('b is bigger')

##
##m=int(input('enter a marks'))#33
##if m>=80:#false
##    print('A grade')
##elif m>=60 and m<80:#false
##    print('B grade')
##elif m>=40 and m<60:#false
##    print('C grade')
##else:
##    print('Failed')
##


##mid="thub@gmail.com"
##ipw='1234'
##
##umid=input('enter a mailid')
##upwd=input('enter password')
##
##if mid==umid and ipw==upwd:
##    print('login succesfully')
##else:
##    print('wrong credentials')


##a=int(input('enter a start range'))#1
##b=int(input('enter a  end range'))#1


##s=int(input('enter a start number '))#5
##e=int(input('enter a end number '))#5
##b=int(input('enter a number '))#4
##if s<=e:#5<=5
##    for n in range(s,e+1):#(5)
##        print(n,'*',b,'=',n*b)
##
##else:
##    for n in range(s,e-1,-1):#(10,9,8,...5)
##        print(n,'*',b,'=',n*b)

##s=int(input('enter a start number '))#5
##e=int(input('enter a end number '))#20
##b=int(input('enter a number '))#4
##for n in range(s,e+1):#(5,6,7,8,....20)
##    if n%2==0:
##        print(n,'*',b,'=',n*b)


##mid="thub@gmail.com"
##ipw='1234'
##for i in range(4):
##    umid=input('enter a mailid')
##    upwd=input('enter password')
##
##    if mid==umid and ipw==upwd:
##        print('login succesfully')
##        break
##    else:
##        print('wrong credentials')
##else:
##    print('account blocked')


##n=int(input('enter a number'))#7
##count=0
##for i in range(1,n+1):#(1,8)#1,2,3,4,5,6,7
##    if n%i==0:#7%1,7%7
##        count+=1#1,2
##
##if count==2:
##    print(n,' is a prime number')
##else:
##    print(n,' is not a prime number')
###############################
##
##n=int(input('enter a number'))#6
##for i in range(2,n):#(2,6) 2
##    if n%i==0:#6%2
##        print(n,' is not a prime number')
##        break
##else:
##    print(n,' is a prime number')

##
##n=int(input('enter a number'))
##i=2
##while i<n:
##    if n%i==0:#6%2
##        print(n,' is not a prime number')
##        break
##    i+=1
##else:
##    print(n,' is a prime number')


##n=int(input('enter a number'))
##count=0
##i=1
##while i<=n:
##    if n%i==0:
##        count+=1
##    i+=1
##    
##if count==2:
##    print(n,' is a prime number')
##else:
##    print(n,' is not a prime number')    

##n=int(input('enter a number'))#153
##s=0
##a=n#153
##while n>0:#153>0,15>0
##    rem=n%10#3,5,1
##    s+=rem*rem*rem#s=s+rem*rem*rem=0+3*3*3=27+5*5*5=152+1*1*1=153
##    n=n//10#15,1
##
##if a==s:
##    print(a,' is Armstrong number')
##else:
##    print(a,' is not a Armstrong number')


##n=int(input('enter a number'))#151
##a=n#151
##rev=0
##while n>0:#151>0,15>0,1>0
##   rem=n%10#1,5,1
##   rev=rev*10+rem#1,10+5=15,150+1=151
##   n=n//10#15,1,0
##if rev==a:
##    print(a,' is palindrome number')
##else:
##    print(a,' is not a palindrome number')
    
##n=int(input('enter a number'))#5
##fact=1
##for i in range(n,0,-1):#(5,4,3,2,1)(1,n+1)
##    fact*=i#fact=fact*i=120
##print(fact)
##
##fact=1
##while n>0:#5,4,3,2,1
##    fact*=n#120
##    n-=1#4,3,2,1,0
##print(fact)
    

##n=int(input('enter a number'))#54
##a=n
##s=0
##while n>0:#54,5
##    rem=n%10#4,5
##    s+=rem#9
##    n//=10#5,0
##if a%s==0:
##    print(a,' is a Harshed number')
##else:
##    print(a,' is not a Harshed number')    

###fibnocci series
##n=int(input('enter a range'))#5  
##a=0
##b=1
##print(a,b,end=" ")
##c=3
##while c<=n:#3,4,5
##    s=a+b#1,2,3
##    print(s,end=" ")
##    a=b#1,1,2
##    b=s#1,2,3
##    c+=1#4,5,6
##
##
##n=int(input('enter a range'))#5  
##a=0
##b=1
##print(a,b,end=" ")
##for i in range(3,n+1):
##    s=a+b#1,2,3
##    print(s,end=" ")
##    a=b#1,1,2
##    b=s#1,2,3

#perfect number
##n=int(input('enter a number'))#6
##s=0
##for i in range(1,(n//2)+1):#(1,2,3)
##    if n%i==0:#6%1,2,3
##        s+=i#1,3,6
##if s==n:
##    print(n,'is a perfect number')
##else:
##    print(n,'is not a perfect number')
#######################
##n=int(input('enter a number'))#6
##s=0
##i=1
##while i<n:#(1,2,3,4,5)1,2,3,4,5
##    if n%i==0:#6%1,2,3
##        s+=i#1,3,6
##    i+=1
##if s==n:
##    print(n,'is a perfect number')
##else:
##    print(n,'is not a perfect number')
##

###before prime number
##a=int(input('enter a starting range'))#23
##for j in range(a-1,1,-1):#(22,21,20,19........2)
##    for i in range(2,j):
##        if j%i==0:
##            #print(j,' is not a prime number')
##            break
##    else:
##        bp=j
##        print(j)
##        break
##
##
####next prime number
###a=int(input('enter a starting range'))#19
##k=a
##while True:
##    for i in range(2,k):
##        if k%i==0:
##            #print(j,' is not a prime number')
##            break
##    else:
##        ap=k
##        print(k)
##        break
##    k+=1
##    
##if (abs(a-ap)>abs(a-bp)):
##    print('nearest prime is ',bp)
##elif (abs(a-ap)==abs(a-bp)):
##    print('nearest prime is ',ap,bp)
##else:
##    print('nearest prime is ',ap)


##n=int(input('enter a range'))#5  
##a=0
##b=1
###print(a,b,end=" ")
##for i in range(3,n+1):
##    s=a+b#1,2,3
##    #print(s,end=" ")
##    a=b#1,1,2
##    b=s#1,2,3
##    if b>=n:
##        print(b)
##        break


##n=int(input('enter a number'))#5
##for i in range(1,n+1):#row 1,2,3,4,5
##    for j in range(1,n+1):#column(1:1,2,3,4,5,,2:1,2,3,4,5)
##        print(i,end=' ')
##    print()


##n=int(input('enter a number'))#5
##for i in range(1,n+1):#row 1 2 3
##    for j in range(1,i+1):#column (1:1,,2:1,2,,3:1,2,3,,4:1,2,3,4,,5:1,2,3,4,5)
##        print(j,end=' ')
##    print()


##n=int(input('enter a number'))#5
##i=1
##while i<=n:#row 1 2 3
##    for j in range(i):#column (1:1,,2:1,2,,3:1,2,3,,4:1,2,3,4,,5:1,2,3,4,5)
##        print('*',end=' ')
##        j+=1
##    print()
##    i+=1


##n=int(input('enter a number'))#5
##for i in range(1,n+1):#1,2
##    for k in range(n,i,-1):#(1:5,4,3,2,,2:5,4,3,,3:5,4,4:5,5:0)
##        print(' ',end=' ')
##    for j in range(1,i+1):#(1:1,,2:1,2,,3:1,2,3,,4:1,2,3,4,,5:1,2,3,4,5)
##        print('*',end=' ')
##    print()


##
##def pattern():
##    n=int(input('enter a number'))#5
##    for i in range(1,n+1):#(1,2,3,4,5),1,2,3
##        print((n-i)*' ',end="")#4    ,3   ,2  ,1 ,0
##        for j in range(1,i+1):#*,,**,,***,****,*****
##            print('*',end='')
##        print()    
##
##
##pattern()
##
##print('example')
##
##pattern()
##
##
##pattern()


##def add(a,b):#(23,25)#formal parameters
##    c=a+b
##    return(c)
##
##a=int(input())#10
##b=int(input())#20
##
##print(add(a,b))#(10,20)#actual parameters
##
##print(add(20,30))

##
##a=10#global variable
##print('start',a)
##
##def example():
##    b=11#local variable
##    print('inside',b)
##
##example()
##
##print('end',b)

##
##a=10
##print('start',a)
##def example():
##    global b
##    b=11
##    print('inside',b)
##    print(b+10)
##example()
##print('end',b)



##a=10
##print('start',a)
##def example():
##    global a
##    a=11
##    print('inside',a)
##example()
##print('end',a)




##def add(a,b):
##    return a+b
##def sub(a,b):
##    return a-b
##def mul(a,b):
##    return a*b
##def div(a,b):
##    return a%b
##a=int(input('enter a number'))
##b=int(input('enter a number'))
##c=int(input('enter a choice 1:add,2:sub,3:mul,4:div'))
##if c==1:
##    print(add(a,b))
##elif c==2:
##    print(sub(a,b))
##elif c==3:
##    print(mul(a,b))
##elif c==4:
##    print(div(a,b))
##else:
##    print('wrong choice')


##def prime(n):
##    for i in range(2,n):#(2,6) 2
##        if n%i==0:#6%2
##            return 0
##            break
##    else:
##        return 1

##
##a=int(input('enter a number'))
##b=int(input('enter a number'))
##d=int(input('enter a number'))
##c=a**2+b**2+d**2
##print(c)

##a,b,d=map(int,input().split())#2 3 4
##c=a**2+b**2+d**2
##print(c)

##a=10
##print(eval('a+1'))
##print(a)
##
##def pattern(n):
##    for i in range(0,n):#row
##        for j in range(n-1,i,-1):#empty spce
##            print(' ',end="")
##        for k in range(0,n):#stars
##            print('*',end="")
##        print()
##n=int(input('enter  a number'))
##pattern(n)


##
##n=5
##for i in range(1,n+1):#row
##    for k in range(n-i,0,-1):#empty
##        print(' ',end="")
##    for j in range(1,n+1):#columns
##        if i==1 or i==n or j==1 or j==n:
##            print('*',end="")
##        else:
##            print(' ',end="")
##    print()

##
##n=10
##for i in range(1,n+1):
##    for j in range(65,65+i):
##        print(chr(j),end="")
##    print()

##n=5
##for i in range(1,n+1):#rows
##    for j in range(1,i+1):#numbers
##        print(j,end="")
##    for k in range(n-i,0,-1):#*
##        print('*',end="")
##    print()

##a=[2,3,6,0,7,3]
##for i in range(0,len(a)):#(0,6),0,1,2,3,4,5
##    print(i,':',a[i])

##a=[2,3,6,0,7,3]
##for i in a:#2,3,6,0,7,3
##    print(i)


##a=['sachin','kohli','rohit','dhoni']
##def length(a):
##    cnt=0
##    for i in a:
##        cnt+=1
##    return (cnt)
##
##print(length(a))


##a=[2,3,4,3,5,8,1,'a','hi',56.765]
##b=int(input('enter a number to check: '))
##cnt=0
##for i in a:#2,3,4,3,5,8,1
##    if i==b:
##        cnt+=1#1,2
##print(cnt)

##
##a=[3,9,4,6,2,5]
##m=a[0]#3
##for i in a:#3,9,4,6,2,5
##    if i<m:#2<3
##        m=i#2
##print(m)
##        
##a=[3,9,1,6,2,5]
##m=a[0]
##for i in a:#3,9,1,6,2,5
##    if i>m:
##        m=i#3,9
##print(m)

##b=[i*i for i in range(1,6)]
##print(b)

##a=[2,43,5,6,0,8,4]
##b=int(input('enter a number: '))#43
##z=0
##for i in a:#2,43
##    if i==b:#2,43
##        print(z)
##        break
##    z+=1#1
##
##a=[2,43,5,6,0,8,4]
##b=int(input('enter a number: '))#43
##for i in range(len(a)):#0,1
##    if b==a[i]:
##        print(i)
##        break


##a=[2,3,6,8,5]
##e=[]
##o=[]
##for i in a:
##    if i%2==0:
##        e.append(i)
##    else:
##        o.append(i)
##print(sum(e))
##print(sum(o))

##a=[2,3,6,8,5,9]#2,6,5    3,8,9
##e=[]
##o=[]
##z=0
##for i in a:#2,3,6,8,5,9
##    if z%2==0:
##        e.append(i)#2,6,5
##    else:
##        o.append(i)#3,8,9
##    z+=1#1,2,3,4,5
##print(sum(e))
##print(sum(o))

##a=[3,4,5,2,6,3,7,2]
##print(a)
##b=[]
##for i in a:#3,4,5,2,6,3,7
##    if i not in b:
##        b.append(i)#[3,4,5,2,6,7]
##
##print(b)

##def prime(n):
##    for i in range(2,n):
##        if n%i==0:
##            return False
##            break
##    else:
##        return True
##a=[7,3,6,4,11,14,17]
##p=[]
##for i in a:#7,3,6,4,11
##    if prime(i)==True:#7,3,11
##        p.append(i)
##print(len(p))

####a=[7,3,6,4,11,14,17]
####cnt=0
####for i in a:#7,3,6,4,11
####    if prime(i)==True:#7,3,11
####        cnt+=1
####print(cnt)
####        

##a=[2,3,4,4,3,2,2,5]
##b=[]
##for i in a:
##    if i not in b:
##        b.append(i)
##c=[]
##for j in b:#[2, 3, 4, 5]
##    c.append(a.count(j))#[3,2,2,1]
##
##print(b[c.index(max(c))])

##a=[2,5,8,9,11,1]
##b=a.copy()
##b.sort()
##if a==b:
##    print('yes')
##else:
##    print('no')
##
##
##a=[2,5,8,4,9,11]
##i=1
##status=True
##while i<len(a):#1,
##    if a[i-1]<a[i]:#
##        status=True
##    else:
##        status=False
##        break
##    i+=1
##print(status)


##a=[2,4,7,5,3]
##b=[4,3,7,9,11]
##for i in a:#2,4,7,5,3
##    if i not in b:
##        print(i)
##

##a=[3,5,4,8,8,7,8]
##a.sort()
##b=[]
##for i in a:
##    if i not in b:
##        b.append(i)
##print(b[-2])

##a=[9,8,5,2,0]
##b=a.copy()
##b.sort(reverse=True)
##if a==b:
##    print('yes')
##else:
##    print('no')

##a=[2,4,7,5,3]
##b=[4,3,7,9,11]
##for i in a:#2,4,7,5,3
##    if i not in b:
##        print(i)
##for j in b:
##    if j not in a:
##        print(j)


##a=['m','sub','i','pyt']
##b=['y','ject','s','hon']
##c=[]
##for i in range(len(a)):
##    c.append(a[i]+b[i])
##print(c)


##a=['my','program']
##b=['python','java']
##c=[]
##for i in a:#my,program
##    for j in b:#python,java,,python,java
##        c.append(i+j)
##print(c)

        
##a=(4,6,2,6,2)
##for i in a:
##    print(i)
##
##for i in range(len(a)):
##    print(a[i])

##a={3,4,5,2,4,5}
##for i in a:
##    print(i)

##
##a={1:5,2:6,3:7}
##for i in a.keys():#key based loop
##    print(i,a[i])
##
##for i in a.values():#value based loop
##    print(i)
##
##for i,j in a.items():#item based loop
##    print(i,j)

##a={}
##for i in range(2):
##    k=input('enter a key')#s1,s2
##    v=[]
##    for j in range(2):
##        m=int(input('enter marks'))#43,34,76,67
##        v.append(m)#[43,34][76,67]
##    a[k]=v#{s1:[43,34],s2:[76,67]}
##print(a)


##
##a='technical'
##b=list()
##b.append('z')
####for i in a:#t,e,c,,h...
####    print(i)
##
##for i in range(len(a)):
##    print(i,a[i])
    
import random
a=['sachin','kohli','rohit','dhoni']
##for i in range(5):
##    #a=random.random()#generates a random float number in between 1 and 0
##    #a=random.uniform(a,b)#generates a random float number in between a and b
##    #a=random.randint(x,y)#generate a integerin between x,y.... x<=a<=y
##    a=random.randrange(1,10,3)#generate a integerin between x,y.... x<=a<y
##    print(a)
##    #print(random.choice(a))
##    


##a=['sachin','kohli','rohit','dhoni']
##print(a)
##for i in range(5):
##    random.shuffle(a)#rearranges the given list
##    print(a)

##a=['sachin','kohli','rohit','dhoni']
##print(a)
##random.shuffle(a)
##print(a)

##a=10
##print(a+b)
##print('hi')


##a=10
##try:
##    print(a+b)  
##except:
##    b=20
##    print(a+b)

##
##a=10
##print(a/0)
##print(a+b)


##a=10
##try:
##    print(a)    
##    print([4,5]/a)
##except NameError:
##    print("avoid naming")
##except ZeroDivisionError:
##    print('can not divide with zero')
##else:
##    print('no error')
##finally:
##    print('done')


##
##def sample(a,b):#formal parameters
##    return(a*b)


##import matplotlib.pyplot as plt
##a=[2,3,4,7]
##b=[4,2,6,9]
###plt.plot(a,b,c='r')
###plt.scatter(a,b,c='r')
###plt.bar(a,b)
##plt.pie(a)
##plt.xlabel('x axis')
##plt.ylabel('y axis')
##plt.title('a axis vs y axis')
##plt.savefig(r'C:\Users\Rajesh\Desktop\filehandling\graph.png')
##plt.show()

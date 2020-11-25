##print even and odd numbers separately##
##a=[2,3,6,8,5]
##e=[]
##o=[]
##for i in a:
##    if i%2==0:
##        e.append(i)
##    else:
##        o.append(i)
##print(e)
##print(o)


##print sum of even and odd numbers##
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


##separate even and odd numbers based on index positions##
##a=[2,3,6,8,5,9]
##e=[]
##o=[]
##z=0
##for i in a:
##    if z%2==0:
##        e.append(i)
##    else:
##        o.append(i)
##    z+=1
##print(e)
##print(o)


##sum of even indexed numbers and odd indexed numbers separately##
##a=[2,3,6,8,5,9]
##e=[]
##o=[]
##z=0
##for i in a:
##    if z%2==0:
##        e.append(i)
##    else:
##        o.append(i)
##    z+=1
##print(sum(e))
##print(sum(o))


##eliminate the duplicates##
##a=[3,4,5,2,6,3,7]
##print(a)
##b=[]
##for i in a:
##    if i not in b:
##        b.append(i)
##print(b)


##find total prime numbers ina list##
##def prime(n):
##    for i in range(2,n):
##        if n%i==0:
##            return False
##            break
##    else:
##        return True
##a=[7,3,6,4,11,14,17]
##p=[]
##for i in a:
##    if prime(i)==True:
##        p.append(i)
##print(len(p))
####OR##
##a=[7,3,6,4,11,14,17]
##count=0
##for i in a:
##    if prime(i)==True:
##        count += 1
##print(count)


##find the second maximum number in the list##
##a=[2,5,6,8,3,8]
##a.sort()
##print(a)


##which element has maximum number of duplicates##
##a=[2,3,4,4,3,2,2,5]
##b=[ ]
##for i in a:
##    if i not in b:
##        b.append(i)
##c=[ ]
##for j in b:
##    c.append(a.count(j))
##print(b[c.index(max(c))])


##element is present in the list or not##
##lis=[2,1,3,6,7,5,4,9,8]
##key=9
##for i in range(len(lis)):
##    if lis[i]==key:
##        print('yes')
##        break
##else:
##    print('no')


##linear search and binary search##
##lis=[2,1,3,6,7,5,4,9,8]
##key=2
##lis.sort()
##i=0
##j=len(lis)-1
##count=0
##while i<=j:
##    m=(i+j)//2
##    if lis[m]==key:
##        print('yes')
##        break
##    elif lis[m]<key:
##        i=m+1
##    else:
##        j=m-1
##    count+=1
    


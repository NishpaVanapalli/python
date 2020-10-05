##a=list(map(int,input().split()))
##print(min(a))


##index based elements accessing##
##a=[2,5,6,9,8,1,4,6]
##for i in range(0,len(a)):
##    print(a[i])


##element based accessing##
##a=[2,5,6,9,8,1,4,6]
##for i in a:
##    print(i)


##len of the list without using keyword##
##a=[4,5,2,6,2,66,9]
##count=0
##for i in a:
##    count += 1
##print(count)


##how many times a no. is repeated in list without using keyword##
##a=[4,5,2,6,2,66,9]
##count=0
##b=int(input('enter a number you want to count: '))
##for i in a:
##    if i==b:
##        count += 1
##print(count)


##find min without using the keyword##
##a=[3,9,4,6,2,5,1]
##m=a[0]
##for i in a:
##    if i<m:
##        m=i
##print(m)


##find max without using the keyword##
##a=[3,9,4,6,2,5,1]
##m=a[0]
##for i in a:
##    if i>m:
##        m=i
##print(m)


##declare list in sequential order##
##a=[i for i in range(10)]
##print(a)
##squares##
##b=[i*i for i in range(10)]
##print(b)


##find index without using the keyword##
##a = [2,43,5,6,0,8,4]
##b = int(input('enter a nmuber: '))
##z=0
##for i in a:
##    if i==b:
##        print(z)
##        break
##    z += 1
##OR##
##a = [2,43,5,6,0,8,4]
##b = int(input('enter a nmuber: '))
##for i in range(len(a)):
##    if b==a[i]:
##        print(i)
##        break



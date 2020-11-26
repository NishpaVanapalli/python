##check whether list is in ascending order or not##
##a=[2,5,8,9,11,1]
##i=1
##status=False
##while i<len(a):
##    if a[i-1]<a[i]:
##        status=True
##    else:
##        status=False
##        break
##    i+=1
##print(status)


##check whether list is in descending order or not##
##a=[2,5,8,9,11,1]
##i=1
##status=False
##while i<len(a):
##    if a[i-1]>a[i]:
##        status=True
##    else:
##        status=False
##        break
##    i+=1
##print(status)
        

##elements present in a but not in b##
##a=[2,4,7,5,3]
##b=[4,3,7]
##for i in a:
##    if i not in b:
##        print(i)


##extra elements present in a and b##
##a=[2,4,7,5,3]
##b=[4,3,7,9]
##for i in a:
##    if i not in b:
##        print(i)
##for j in b:
##    if j not in a:
##        print(j)


##list strings##
##a=['m' , 'sub' , 'i' , 'pyt']
##b=['y' , 'ject' , 's' , 'hon']
##c=[ ]
##for i in range(len(a)):
##    c.append(a[i]+b[i])
##print(c)


##list strings2##
##a=['my' , 'program']
##b=['python' , 'java']
##c=[ ]
##for i in a:
##    for j in b:
##        c.append(i+j)
##print(c)


##tuple 1##
##a=(4,6,2,6,2)
##for i in a:
##    print(i)
##or##
##for i in range(len(a)):
##    print(a[i])


##set##
##a={3,4,5,2,4,5}
##for i in a:
##    print(i)
    

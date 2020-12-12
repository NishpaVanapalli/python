##a={1:5,2:3,3:4}
##a.pop(3)
##print(a)


##my_tuple = (1, 2, 3, 4)
##my_tuple.append( (5, 6, 7) )
##print (len(my_tuple))


##nums = set([1,1,2,3,3,3,4,4])
##print(len(nums))


##a={1:"A",2:"B",3:"C"}
##print(a.get(1))


##a={1:"A",2:"B",3:"C"}
##a.setdefault(4,"D")
##print(a)


##a={1:"A",2:"B",3:"C"}
##b={4:"D",5:"E"}
##a.update(b)
##print(a)


##d1 = {"john":40, "peter":45}
##d2 = {"john":466, "peter":45}
##print(d1 == d2)


##a={'B':5,'A':9,'C':7}
##print (sorted(a))


##numbers = {}
##letters = {}
##comb = {}
##numbers[1] = 56
##numbers[3] = 7
##letters[4] = 'B'
##comb['Numbers'] = numbers
##comb['Letters'] = letters
##print(comb)


##a=(1,2,3)
##b=('A','B','C')
##c=zip(a,b)
##print(list(c))


##a = {}
##a[1] = 1
##a['1'] = 2
##a[1]=a[1]+1
##count = 0
##for i in a:
##    count += a[i]
##print(count)


##a={1:"A",2:"B",3:"C"}
##for i in a:
##    print(i,end=" ")


##count={}
##count[(1,2,4)] = 5
##count[(4,2,1)] = 7
##count[(1,2)] = 6
##count[(4,2,1)] = 2
##tot = 0
##for i in count:
##    tot=tot+count[i]
##print(len(count)+tot)


##a={"a":1,"b":2,"c":3}
##b=dict(zip(a.values(),a.keys()))
##print (b)


##t=("Hello",)*3
##print (t)


##total={}
##def insert(items):
##    if items in total:
##        total[items] += 1
##    else:
##        total[items] = 1
##insert('Apple')
##insert('Ball')
##insert('Apple')
##print (len(total))


##d = {"john":40, "peter":45}
##print(list(d.keys()))


##d1 = {"john":40, "peter":45}
##d2 = {"john":466, "peter":45}
##print(d1 > d2)


##a=(1,2,(4,5))
##b=(1,2,(3,4))
##print (a<b) 


##a={}
##print (a.fromkeys([1,2,3],"check") )


##a=(1,2,3)
##b=('A','B','C')
##c=zip(b,a)
##print (tuple(c))


##d = {"john":40, "peter":45}
##"john" in d


##a = {}
##a[1] = 1
##a['1'] = 2
##a[1.0]=4
##count = 0
##for i in a:
##    count += a[i]
##print(count)

##a=10
##b=20
##def sample(a,b):
##    print(a+b)
##sample(a,b)
##sample(25,30)


##a=10
##b=20
##def sample(a,b):
##    return(a+b)
##print(sample(10,20))


##a=10
##b=20
##def sample(a,b):
##    return(a+b)


##import math
##print(math.sin(45))


import matplotlib.pyplot as plt
a=[2,3,4,7]
b=[4,5,6,9]
plt.plot(a,b)
plt.show()
plt.scatter(a,b)
plt.plot(a,b,c='r')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('x axis vs y axis')
plt.bar(a,b)
plt.pie(a)
a=[ ]
b=[ ]
plt.savefig(r'NISHPA(D:)\graph.jpeg')

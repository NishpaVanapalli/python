##b=list(set(branches))
##data={}
##for r in b:
##    data[r]=branches.count(r)
##data={k:v for k, v in sorted (data items(),key= lambda x:x[1])}
##for k in data.keys():
##    print(k,'-->',data[k])


##import csv
##data=[]
##with open("data.csv") as file1:
##    records=list(csv.reader(file1))
##    for record in records[1:]:
##        data.append(record)
##print(len(data))
##d23=[]
##for d in data:
##    if d[-1]=='2023':
##        d23.append(d)
##print(len(d23))
##c=1
##with open("2023.csv","w",newline="\n") as file2:
##    w1=csv.writer(file2)
##    for d in d23:
##        d[0]=c
##        c+=1
##        w1.writerow(d)



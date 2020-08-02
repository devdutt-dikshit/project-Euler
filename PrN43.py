import time
t1=time.time()
import itertools
l=list(int(''.join(k)) for k in itertools.permutations('0123456789'))
t2=time.time()
flag=0
x=[]
for i in l:
    j=str(i)
    if int(j[1:4])%2==0 and int(j[2:5])%3==0 and int(j[3:6])%5==0 and int(j[4:7])%7==0 and int(j[5:8])%11==0 and int(j[6:9])%13==0 and int(j[7:10])%17==0:
        x.append(i)
print(x)                                
print(t2-t1)
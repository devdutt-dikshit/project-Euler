y=[]
import time
t1=time.time()
for i in range(101,1000):
    for j in range(1,i):
        if len(str(j)+str(i)+str(i*j))==9 and sorted(str(j)+str(i)+str(i*j))==sorted('391867254'): 
            y.append(i*j)
print(set(y))
sum=0
for k in set(y):
    sum=sum+k
t2=time.time()
print(sum)
print(t2-t1)

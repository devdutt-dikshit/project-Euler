import math
import time
t1=time.time()
big=[]
num=0
list_1=tuple(range(1,1000))
for k in list_1:
    list_of_all_answers=[]
    for i in range(1,k):
        for j in range(1,i):
            t_s=int(math.sqrt((i*i)+(j*j)))
            if (t_s+i+j)!=k or (t_s*t_s)!=(i*i)+(j*j):
                continue
            elif (t_s+i+j)==k and (t_s*t_s)==(i*i)+(j*j):
                list_of_all_answers.append((j,i,t_s))
                if len(big)==0:
                    big=list_of_all_answers
                if len(list_of_all_answers)>len(big):
                    big=list_of_all_answers
                    num=k
print(big,num)
t2=time.time()
print(t2-t1)

# max time is in that program is 150sec.and the answer is 840
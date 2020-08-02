
#problem no 34:

import math
x=[]
for i in range(10000000):
    data=0
    x=list(str(i))
    for j in range(len(x)):
        data=data+math.factorial(int(x[j]))
    if (data==i):
        if data==1 or data==2:
            pass
        else:
            print(data)
        
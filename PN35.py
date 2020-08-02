# Problem No. 35
import time
import math
t1=time.time()
y=[]
def is_prime(n):
    if n<=1:
        return False
    max_div=math.floor(math.sqrt(n))
    for i in range(2,1+max_div):
        if n%i==0:
            return False
    return True
for i in range(1,1000000):
    if is_prime(i):
        y.append(i)

l=[k for k in y if k>=11]
primes = set(y)
from itertools import permutations
d=[k for k in y if k<11]
for i in l:
    value=set([int(''.join(k)) for k in permutations(str(i))])
    if value <= primes:
        d.append(i)
print(sorted(d))
t2=time.time()
print(t2-t1)

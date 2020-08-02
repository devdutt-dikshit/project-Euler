import math
x=[]
all_prime=[]
big=0          
def is_prime(n):
    if n<=1:
        return False
    max_div=math.floor(math.sqrt(n))
    for i in range(2,1+max_div):
        if n%i==0:
            return False
    return True
user_input=input("Enter The value: ")
str1=''
for i in range(1,(int(user_input)+1)):
    str1=str1+str(i)
for num in range(int(str1),int(str1[::-1])):
    if sorted(str(num))==sorted(str1):
            x.append(num)
for i in x:
    if is_prime(i):
        all_prime.append(i)
for i in all_prime:
    if i>=big or big==0:
        big=i
print(big)



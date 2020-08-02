
import math
a=[2,3]
for i in range(5,10000,2):
    prime=True
    max_f = math.ceil(math.sqrt(i))
    for j in a:
        if j>max_f:
            break
        if i%j==0:
            prime=False
            break
    if prime:
        a.append(i)
new_list_right=[]
new_list_left=[]
def is_left(ele):
    flag=True
    rem_ele=ele
    for i in range(len(str(ele))):
        rem_ele=str(rem_ele)
        rem_ele=rem_ele[1:]
        # print(rem_ele)
        while(rem_ele[0:1]=='0'):
            rem_ele=rem_ele[1:]
        if len(rem_ele)>1:
            if int(rem_ele) not in a:
                flag=False
                break
        if len(str(rem_ele))==1 and flag:
            new_list_left.append(ele)
            break
        
def is_right(ele):
    flag=True
    rem_ele=ele
    for i in range(len(str(rem_ele))):
        rem_ele=int(rem_ele/10)
        if rem_ele not in a:
            flag=False
            break
        if len(str(rem_ele))==1 and flag:
            new_list_right.append(ele)
# print(a)
for i in a:
    is_left(i)
    is_right(i)
# print(new_list_right)
# print(new_list_left)
print(sorted(list(set(new_list_left) & set(new_list_right))))
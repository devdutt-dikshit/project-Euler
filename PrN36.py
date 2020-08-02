# PN36
def palindromic(i):
    flag=False
    i=str(i)
    if i==i[::-1]:
        flag = True
    return flag
def com_binary(n):
    binary=''
    while(n!=0):
        if n%2!=0:
            binary=binary+'1' 
        else:
            binary=binary+'0'
        n=int(n/2)
    if palindromic(binary):
        return True
    else:
        return False
x=list(range(1,100000))
y=[]
for i in x:
    if com_binary(i) and palindromic(i):
        y.append(i)
print(y)

        
        
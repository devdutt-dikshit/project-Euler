big=0
for i in range(1,100000):
    prod1=''
    for j in range(1,9):
        prod1=prod1+str(i*j)
        if len(prod1)==9:
            break
    if len(prod1)==9:
        if sorted(prod1)==sorted('123456789'):
            if int(prod1)>big:
                big=int(prod1)
                num=i
            if big==0:
                big=int(prod1)
                num=i
print(big,num)
        
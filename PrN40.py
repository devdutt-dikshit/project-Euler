val=''
for i in range(1,100000):
    val=val+str(i)
def fractional(d_val):
    return int(val[d_val-1:d_val])
prod,j=1,1
for i in range(1,7):
    prod=prod*fractional(j)
    j=j*10
print(prod)

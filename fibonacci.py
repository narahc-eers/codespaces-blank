s=0
n=1
for i in range(14):
    print (str(i+1) + " , " + str(s))
    temp = s + n
    s = n
    n=temp
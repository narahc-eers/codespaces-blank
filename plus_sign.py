x = " "
k = "_"
for i in range(80):
    if i == 39:
        for f in range(80):
            print(k)
    s = " "
    for j in range(80):
        s = s + x
        if j == 39:
            s = s + "|"
    print(s)
    

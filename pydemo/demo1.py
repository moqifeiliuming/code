i=9
while i>=1:
    j=1
    while j <= i:
        print("%d*%d=%2d\t"%(j,i,j*i),end = '')
        j+=1
        pass
    i-=1;
    pass
    print()

i=1
while i<=9:
    j=1
    while j<=i:
        print("%d*%d=%2d\t"%(j,i,j*i),end=' ')
        j+=1
        pass
    i+=1
    pass
    print()

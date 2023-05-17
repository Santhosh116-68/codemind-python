def add(n):
    m=0
    while(n>0):
        h=n%10
        m=m+h
        n=n//10
    if(m<10):
        print(m)
    else:
        add(m)
a=int(input())
if(a<10):
    print(a)
else:
    n=int(a)
    add(a)

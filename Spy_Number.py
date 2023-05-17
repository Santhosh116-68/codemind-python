def hi(n):
    m=0
    b=1
    while(n>0):
        h=n%10
        m=m+h
        b=b*h
        n=n//10
    if(m==b):
        print("Spy Number");
    else:
        print("Not Spy Number");
n=int(input())
hi(n)
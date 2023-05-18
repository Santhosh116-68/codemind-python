def sofs(n):
    m=0
    while(n):
        h=n%10
        m=m+(h*h)
        n//=10
    if(m>=10):
        sofs(m)
    else:
        if(m==1 or m==7):
            print("True")
        else:
            print("False")
n=int(input())
sofs(n)
    
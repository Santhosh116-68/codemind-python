def isprime(n):
    c=0
    for i in range(1,n+1):
        if(n%i==0):
            c+=1
    if(c==2):
        return 1
    else:
        return 0
n=int(input())
x=0
z=0
a=n
c=isprime(n)
if(c!=1):
    print("Not Mega Prime")
else:
    while(a):
        l=a%10
        p=isprime(l)
        x+=1
        if(p==0):
            break
        else:
            z+=1
        a//=10
    if(x==z):
        print("Mega Prime")
    else:
        print("Not Mega Prime")
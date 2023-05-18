n,m=map(int,input().split())
h=max(n,m)
for i in range(1,h+1):
    if(n%i==0 and m%i==0):
        l=i
print(l)
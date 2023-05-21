n=int(input())
l=list(map(int,input().split()))
a=0
b=0
for i in range(n):
    if i%2==0:
        a+=l[i]
    else:
        b+=l[i]
if a>b:
    print(int(a-b))
else:
    print(int(b-a))
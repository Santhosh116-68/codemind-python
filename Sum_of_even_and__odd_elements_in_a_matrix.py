r,c=map(int,input().split())
a=[]
even=0
odd=0
for i in range(r):
    lst=list(map(int,input().split()))
    a.append(lst)
for i in range(r):
    for j in range(c):
        if a[i][j]%2==0:
            even=even+a[i][j]
        else:
            odd+=a[i][j]
print(even,odd)
    
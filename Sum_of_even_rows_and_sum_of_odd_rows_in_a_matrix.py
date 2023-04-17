r,c=map(int,input().split())
a=[]
even=0
odd=0
for i in range(r):
    lst=list(map(int,input().split()))
    a.append(lst)
for i in range(r):
    if i%2==0:
        even=even+sum(a[i])
    else:
        odd+=sum(a[i])
print(even,odd)
    
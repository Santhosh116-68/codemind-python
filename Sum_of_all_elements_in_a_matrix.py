r,c=map(int,input().split())
a=[]
su=0
for i in range(r):
    lst=list(map(int,input().split()))
    a.append(lst)
for i in range(r):
    for j in range(c):
        su+=a[i][j]
print(su)
    
n=int(input())
m=0
for i in range(1,n):
    if(n%i==0):
        m=m+i
if(m==n):
    print("True")
else:
    print("False")
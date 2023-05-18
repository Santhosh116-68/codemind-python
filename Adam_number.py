def reverse(a):
    m=0
    while(a):
        h=a%10
        m=m*10+h
        a//=10
    return m

n=int(input())
s=n*n
a=reverse(n)
s2=a*a
s1=reverse(s2)
if(s1==s or n==0):
    print("True")
else:
    print("False")
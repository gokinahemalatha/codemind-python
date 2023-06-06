n=int(input())
s=n*n
k=0
while n>0:
    d=n%10
    n=n//10
    k=(k*10)+d
m=k*k
l=0
while m>0:
    x=m%10
    m=m//10
    l=(l*10)+x
if l==s:
    print('True')
else:
    print('False')
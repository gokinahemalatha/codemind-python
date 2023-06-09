n=int(input())
a=0
b=1
c=a+b
print(a,b,end=' ')
i=2
while(i<n):
    print(c,end=' ')
    t=a
    a=b
    b=c
    c=a+b
    i+=1
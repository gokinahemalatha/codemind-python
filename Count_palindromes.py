def palin(n):
    rev=0
    temp=n
    while(n):
        r=n%10
        n=n//10
        rev=rev*10+r
    if(rev==temp):
        return 1
    else:
        return 0
s=int(input())
c=0
a=list(map(int,input().split()))
for i in a:
    if(palin(i)):
        c+=1
print(c)
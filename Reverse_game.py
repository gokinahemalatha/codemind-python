def reverse(n):
    rev=0
    while(n):
        r=n%10
        n=n//10
        rev=rev*10+r
    return rev
s=int(input())
c=0
b=[]
a=list(map(int,input().split()))
for i in a:
    b.append(reverse(i))
print(*b)
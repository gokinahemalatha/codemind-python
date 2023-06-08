n=int(input())
a=list(map(int,input().split()))
max=0
for i in a:
    c=0
    while(i):
        d=i%10
        i=i//10
        c+=1
    if c>max:
        max=c
s=0
for i in a:
    c=0
    while(i):
        d=i%10
        i=i//10
        c+=1
    if c==max:
        s+=1
print(s)
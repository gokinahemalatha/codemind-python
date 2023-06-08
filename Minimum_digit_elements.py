n=int(input())
a=list(map(int,input().split()))
min=999
for i in a:
    c=0
    while(i):
        d=i%10
        i=i//10
        c+=1
    if c<min:
        min=c
s=0
for i in a:
    c=0
    while(i):
        d=i%10
        i=i//10
        c+=1
    if c==min:
        s+=1
print(s)
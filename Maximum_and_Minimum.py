n=int(input())
a=list(map(int,input().split()))
c=0
b=[]
min=999
max=0
for i in a:
   if a.count(i)==i:
        if i>max:
           max=i
           c+=1
        if i<min:
            min=i
            c+=1
if c==0:
    print(-1)
else:
    print(min,max,end=' ')
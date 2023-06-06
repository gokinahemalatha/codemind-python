n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    s=s+i
avg=s/n
print('{:.2f}'.format(avg))
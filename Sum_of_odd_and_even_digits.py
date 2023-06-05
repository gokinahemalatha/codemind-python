n=int(input())
a=list(map(int,input().split()))
es=0
os=0
for i in range(len(a)):
    if i%2==0:
        es=es+a[i]
    else:
        os=os+a[i]
if(es-os==0):
    print('YES')
else:
    print('NO')
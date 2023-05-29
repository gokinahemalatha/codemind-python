n=int(input())
c=n
for i in range(1,n+1):
    for j in range(i,n+1):
        print(chr(64+c),end=' ')
    c-=1
    print()
    
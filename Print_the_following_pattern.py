n=int(input())
t=n
for i in range(0,n):
    for j in range(0,n):
        if i==j or j==n-i-1:
            print(t,end=' ')
        else:
            print(end=' ')
    t-=1
    print()
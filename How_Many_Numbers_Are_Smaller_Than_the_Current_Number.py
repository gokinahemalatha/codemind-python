n=input()
a=list(map(int,input().split()))
for i in range(len(a)):
    c=0
    for j in range(len(a)):
        if i==j:
            continue
        if a[i]>a[j]:
            c+=1
    print(c,end=' ')
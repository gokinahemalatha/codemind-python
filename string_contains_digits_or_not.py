T=int(input())
for t in range(1,T+1):
    s=input()
    c=0
    for i in s:
        if i>='0' and i<='9':
            c=1
    if c==0:
        print('No')
    else:
        print('Yes')
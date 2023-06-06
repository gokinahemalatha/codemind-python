t=int(input())
while(t):
    s=input()
    b=[]
    c=0
    for i in s:
        b.append(i)
    for i in range(len(b)-1):
        if b[i]==b[i+1]:
            c+=1
    print(c)
    t-=1
def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
n=n+1
while(n>0):
    r=0
    t=n
    while(t):
        d=t%10
        r=r*10+d
        t=t//10
    if r==n:
        if prime(n):
            print(n)
            break
    n+=1
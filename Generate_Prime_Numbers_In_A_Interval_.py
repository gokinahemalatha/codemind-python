def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
l=int(input())
r=int(input())
for i in range(l,r+1):
    if i==1:
        continue
    if(prime(i)):
        print(i)
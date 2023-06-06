n=int(input())
def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return True
    else:
        return False
c=0
for i in range(1,n+1):
    if i==1:
        c=1
    if n%i==0:
        if prime(i):
            c+=1
print(c)
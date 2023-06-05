n1=int(input())
a=list(map(int,input().split()))
s=list(set(a))
s.sort()
n=len(s)
if n>=3:
    print(s[-3])
else:
    print(s[-1])
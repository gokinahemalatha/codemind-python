s=input()
c=0
m=0
for i in range(len(s)):
    b=''
    for j in range(i,len(s)):
        b+=s[j]
        l=b[::-1]
        if l==b:
            if len(b)>m:
                c+=1
                m=len(b)
                k=b
if c==0:
    print(-1)
else:
    print(k)
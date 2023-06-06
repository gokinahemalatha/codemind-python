s=input()
v='aeiouAEIOU'
s1=s.split()
c=0
for i in s1:
    s2=''
    c+=1
    if i[0] in v:
        k=c
        s2+=i+'ma'
        while(k):
            s2+='a'
            k-=1
        print(s2,end=' ')
    else:
        k=c
        s2+=i[1:]+i[0]+'ma'
        while(k):
            s2+='a'
            k-=1
        print(s2,end=' ')
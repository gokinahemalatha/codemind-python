s=input().lower()
m=0
for i in s:
    if s.count(i)>m:
        m=s.count(i)
c=0
l=[]
for i in s:
    if int(s.count(i)/m)==1:
            continue
    else:
        c+=1
        l.append(s.count(i))
if c==0:
    print('Valid String')
elif c==1 and l[0]==(m-1):
    print('Valid String')
else:
    print('Not Valid')
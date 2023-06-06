s1,s2=map(str,input().split())
c=0
for i in s1:
    if s1.count(i)<=s2.count(i):
        continue
    else:
        c=1
        break
if c==1:
    print('False')
else:
    print('True')
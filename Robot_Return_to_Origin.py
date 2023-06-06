s=input()
x=0
y=0
for i in s:
    if i=='R':
        x+=1
    if i=='L':
        x-=1;
    if i=='U':
        y+=1
    if i=='D':
        y-=1
if x==0 and y==0:
    print('True')
else:
    print('False')
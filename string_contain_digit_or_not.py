s=input()
c=0
for i in s:
    if i>='0' and i<='9':
        c+=1
m="'"
if c==0:
    print('Doesn{0}t contain digit'.format(m))
else:
    print('Contains {0} digit'.format(c))
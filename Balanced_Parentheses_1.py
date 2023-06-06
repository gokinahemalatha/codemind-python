s=input()
s1=[]
for i in s:
    if i=='(' or i=='[' or i=='{':
        s1.append(i)
    if i==')' and len(s1)!=0 and s1[-1]=='(':
        s1.pop()
    if i==']' and len(s1)!=0 and s1[-1]=='[':
        s1.pop()
    if i=='}' and len(s1)!=0 and s1[-1]=='{':
        s1.pop()
if len(s1)==0:
    print('True')
else:
    print('False')

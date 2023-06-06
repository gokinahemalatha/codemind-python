s=input()
b=[]
for i in s:
    if i.isalpha():
        b.append(i)
c=len(b)-1
l=""
for i in range(len(s)):
    if s[i].isalpha():
        l+=b[c]
        c-=1
    else:
        l+=s[i]
print(l)
s=input()
m='aeiouAEIOU'
s1=" "
s2=''
for i in s:
    if i in m:
        s1+=i
c=0
for i in range(len(s)):
    if s[i] in m:
        c+=1
        s2+=s1[len(s1)-c]
    else:
        s2+=s[i]
print(s2)
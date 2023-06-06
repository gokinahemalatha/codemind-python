s=input()
a='aeiouAEIOU'
b=[]
m=0
for i in range(len(s)):
    if s[i] in a:
        c=1
        for j in range(i+1,len(s)):
            if s[j] in a:
                   c+=1
            else:
                break
        b.append(c)
print(max(b))
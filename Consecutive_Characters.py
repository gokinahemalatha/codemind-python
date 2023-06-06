s=input()
b=[]
m=0
for i in range(len(s)):
    c=1
    for j in range(i+1,len(s)):
        if s[i]!=s[j]:
            break
        else:
            c+=1
    b.append(c)
print(max(b))
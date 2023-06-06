s=input()
c=1
for i in range(1,len(s)):
    if s[i].isupper() and s[i+1].islower():
        c+=1
    
print(c)
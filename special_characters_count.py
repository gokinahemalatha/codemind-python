s=input()
a='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
c=0
for i in s:
    if i==' ':
        continue
    if i not in a:
        c+=1
print(c)
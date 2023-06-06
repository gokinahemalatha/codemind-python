s=input()
max=0
b='aeiou'
c=0
for i in s:
    if i in b:
        c+=1
        if c>max:
            max=c
    else:
        c=0
print(max)
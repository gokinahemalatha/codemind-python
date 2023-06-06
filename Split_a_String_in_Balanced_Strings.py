def bss(s):
    m=0
    e=0
    c=0
    for i in s:
        if i=='L':
            e+=1
        else:
            c+=1
        if e==c:
            m+=1
    return m
s=input()
print(bss(s))
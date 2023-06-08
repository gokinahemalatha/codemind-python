s=input()
c=input()
for i in range(len(s)):
    if s[i]==c:
        print('True')
        print(i)
        break
else:
    print('False')
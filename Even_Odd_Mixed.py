a=int(input())
even=0
odd=0
while a:
    d=a%10
    if(d%2==0):
        even+=1
    else:
        odd+=1
    a=a//10
if(even==0):
    print('Odd')
elif(odd==0):
    print('Even')
else:
    print("Mixed")
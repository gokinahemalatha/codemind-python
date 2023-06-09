T=int(input())
for t in range(1,T+1):
    n=int(input())
    for i in range(1,n):
        if(i*i==n):
            print('True')
            break
    else:
        print('False')
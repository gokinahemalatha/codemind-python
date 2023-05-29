t=int(input())
for i in range(0,t):
    n=int(input())
    a=[int(x) for x in input().split()]
    if n==1:
        print(0)
    else:
        b=[]
        for i in a:
            if i in range(1,10000000,2):
                b.append(i)
        if len(b)==1:
            
            print(0)
        elif len(b)%2==0:
            
            print(int(len(b)/2))
        else:
            print(int((len(b)-1)/2))
                    
                
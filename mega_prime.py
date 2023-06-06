n=int(input())
c=0
dc=0
s=0
for i in range(1,n+1):
   if n%i==0:
      c+=1
if c==2:
   while n:
      d=n%10
      n=n//10
      dc+=1
      fc=0
      for i in range(1,d+1):
          if d%i==0:
             fc+=1
      if fc==2:
         s+=1
   if s==dc:
      print('Mega Prime')
   else:
      print('Not Mega Prime')
else:
   print('Not Mega Prime')
s=input()
st=[]
st2=[]
k=0
for i in s:
    if i=='(':
        st.append(i)
    elif i=='*':
        st2.append(i)
    else:
        if len(st)==0:
            if len(st2)==0:
                k=1
                break
            else:
                st2.pop()
        else:
            st.pop()

if len(st)==0 and k==0:
    print('True')
else:
    print('False')
s=input('enter the string:')
l=len(s)
c=0
for i in range(l):
    if 'o'==s[i]:
        c=c+1
if(c!=0):
    print('occurrence of c:'+str(c))
else:
    print('o is not present')

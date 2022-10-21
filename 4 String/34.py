s=input('enter the string:  ')
l=len(s)
for i in range(l):
    p=s[i]
    c=s.count(p)
    if(c==1):
        break
print(p)
      



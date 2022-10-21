s=input('enter string: ')
l=len(s)
p=s[:4]
c=0
for i in p:
    if(i.isupper()):
        c=c+1
if(c==2):
    print(s.upper())
else:
    print(s)
    

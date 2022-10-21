s=input('enter the string:  ')
d={}
for i in range(97,124):
    p=chr(i)
    c=s.count(p)
    if(c!=0):
        d[p]=c
        '''print(p+ " repeatation: " +str(c))'''
print(d)
      

s=input('enter the string:  ')
l=s.split()
for i in l:
    c=s.count(i)
    if(c>1):
        print(i)
        break
      

s=input('enter the string:  ')

for i in range(97,124):
    p=chr(i)
    c=s.count(p)
    if(c>1):
        print('first repeated charac. '+ p)
        break
      

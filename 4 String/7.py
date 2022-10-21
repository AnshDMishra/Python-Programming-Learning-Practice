n=int(input('how many words u want to enter: '))
l=[input('enter word'+str(i+1)) for i in range(n)]
s=[len(k) for k in l]
print('length of longest one:',max(s))
      

s=input('enter the string:')
space=s.count(' ')
l=s.split()
#print(space)
#print(l)
for i in range(space):
    print(' ',end='')
print(''.join(l))
      



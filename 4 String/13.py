sen=input('enter string:')
k=sen.split()
i=int(input('enter position at which u want to enter a string'))
s=input('enter string u want to enter in middle')
k.insert(i,s)
print(' '.join(k))

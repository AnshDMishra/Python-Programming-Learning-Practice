s=input('enter the string:')
l=list(s)
for i in l:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        l.remove(i)
print(''.join(l))

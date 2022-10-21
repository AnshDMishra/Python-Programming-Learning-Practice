s=input('enter string: ')
l=len(s)
if l%4==0:
    p=s[-1::-1]
    print(p)
else:
    print(s)

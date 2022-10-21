s=input('enter string ')
c=input('enter character u want to strip')
if c in s:
    print(s.strip(c))
else:
    print(s)

s=input('enter string with . and ,:')
p='.,'
q=',.'
r=s.maketrans(p,q)
print(s.translate(r))

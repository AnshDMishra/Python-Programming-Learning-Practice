s=input('enter string ')
n=int(input('enter number of char u want in lowercase'))
p=s[:n-1]
q=s[n:]
r=p.lower()
print(r+q)

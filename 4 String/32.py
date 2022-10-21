s=input('enter string :')
l=len(s)
p=q=r=k=t=0
if 'a' in s:
    for i in range(l):
        p=p+1
if 'e' in s:
     for j in range(l):
        q=q+1
if 'i' in s:
    for k in range(l):
        r=r+1
if 'o' in s:
    for m in range(l):
        k=k+1
if 'u' in s:
    for n in range(l):
        t=t+1
print("a",p)
print("e",q)
print("i",r)
print("o",k)
print("u",t)

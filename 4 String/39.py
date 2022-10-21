s=input('enter the string:  ')

b=set(s)
l=list(b)
q=[]
#print(b)
#print(l)
for i in l:
    c=s.count(i)
    q.append(c)
#print(q)
r=sorted(q)
#print(r)
j=r[-2]
ind=q.index(j)
print('second most repeated element:',l[ind])

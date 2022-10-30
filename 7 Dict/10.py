n=int(input('enter n:'))
d={x:x*x for x in range(1,n+1)}
print(d)
k=int(input('enter key u want to remove:'))
del d[k]
print(d)


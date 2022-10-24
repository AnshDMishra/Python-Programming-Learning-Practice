x=int(input("how many numbers u want to enter at least 7:"))
l=[]
for i in range(x):
    v=input('enter value:')
    l.append(v)
print(l)
del l[4:6]
del l[0]
print(l)

x=int(input("how many numbers u want to enter"))
l=[int(input("enter no.: ")) for i in range(x)]
print(l)
for i in l:
    c=l.count(i)
    if(c>1):
        l.remove(i)
print(l)


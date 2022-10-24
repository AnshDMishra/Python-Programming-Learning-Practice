x=int(input("how many numbers u want to enter"))
l=[int(input("enter no.: ")) for i in range(x)]
print(l)
for i in l:
    if i%2==0:
        l.remove(i)
print(l)

x=int(input("how many numbers u want to enter"))
l=[int(input("enter no.: ")) for i in range(x)]
print(l)
s=set(l)
l1=list(s)
print('list with unique values:',l1)

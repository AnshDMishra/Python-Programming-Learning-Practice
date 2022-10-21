x=int(input("how many numbers u want to enter"))
l=[int(input("enter no.: ")) for i in range(x)]
l1=sorted(l)
print(l1)
print('sencond larest no:',l1[len(l1)-2])

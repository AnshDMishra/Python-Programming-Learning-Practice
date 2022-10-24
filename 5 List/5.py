x=int(input("how many numbers u want to enter"))
l=[int(input("enter no.: ")) for i in range(x)]
print(l)
c=len(l)
if(c==0):
    print('empty')
else:
    print('not empty')

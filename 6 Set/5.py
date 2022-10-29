s={input("enter element: ") for i in range(5)}
print(s)
i=input("enter member u want to remove: ")
if i in s:
    s.remove(i)
    print(s)
else:
    print('item does not present')

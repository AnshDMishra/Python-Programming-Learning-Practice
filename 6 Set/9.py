s1={input("enter element: ") for i in range(5)}
print('set1->',s1)
s2={input("enter element: ") for i in range(5)}
print('set2->',s2)
print('symmetric difference is',s1.symmetric_difference(s2))

"""
17. Write a Python program to get the top three items in a shop.
    Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}

    Expected Output:
        item4 55
        item1 45.5
        item3 41.3
"""
d={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
#print(d.items())
list_of_tuples=d.items()
#print(sorted(list_of_tuples))

def sort_basis(item):
	return item[1]

#print(sorted(list_of_tuples,key=sort_basis))
#print(sorted(list_of_tuples,key=sort_basis,reverse=True))

list=sorted(d.items(),key=sort_basis,reverse=True)
d1=dict(list[:3])
print(d1)


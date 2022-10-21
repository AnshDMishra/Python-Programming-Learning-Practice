'''
13. Write a Python program to remove duplicates(based on values) from Dictionary.
'''

d = {1:10, 2:20, 3:30, 4:40, 5:10, 6:20}
d2 = {}
for k,v in d.items():
  if v not in d2.values():
    d2[k] = v
print(d2)

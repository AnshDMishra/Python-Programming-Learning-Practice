'''
16. Write a Python program to print a dictionary in table format.

'''

d = {101:'Ram', 102:'Mohan', 103:'Karan'}
print("\tKEY  :\tNAME")
for k, v in d.items():
  print('\t{}  : \t{}'.format(k,v))

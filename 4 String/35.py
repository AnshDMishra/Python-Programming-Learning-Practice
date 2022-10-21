"""
35. Write a Python program to print all permutations with given repetition number of characters of a given string.  
"""
from itertools import permutations 
k=list(permutations(input('Enter a word : ')))
l=[]
for i in k:
    s=''.join(i)
    l.append(s)
print(len(l))


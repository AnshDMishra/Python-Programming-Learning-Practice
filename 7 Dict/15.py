"""
15. Write a Python program to combine two dictionary adding values for common keys.

    d1 = {'a': 100, 'b': 200, 'c':300}
    d2 = {'a': 300, 'b': 200, 'd':400}

    Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
"""
#d1={input('Key : '):int(input('Value(Number) : ')) for i in range(int(input('Enter length of dict 1 : ')))}
#d2={input('Key : '):int(input('Value(Number) : ')) for i in range(int(input('Enter length of dict 2 : ')))}
from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d = Counter(d1)+Counter(d2)
print(d)

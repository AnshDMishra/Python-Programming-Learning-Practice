##16. Write a Python program to get a char in a string just before a
##specified substring.

s=input("Enter the string: ")
sub=input("Enter the substring: ")
if (sub in s):
    i=s.index(sub)
    print(f"The last character before the sub-string is {s[i-1]}")
else:
    print(f"The sub-string'{sub}' does not exist in '{s}'")

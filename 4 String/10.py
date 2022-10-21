sen=input('enter sentence:')
l=sen.split()
s=set(l)
for i in s:
    c=sen.count(i)
    print(i,c)

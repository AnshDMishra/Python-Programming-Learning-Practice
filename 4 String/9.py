s=input('enter string: ')
l=len(s)
fs=""
for i in range(l):
    if(i%2==0):
       fs=fs+s[i]
print(fs)


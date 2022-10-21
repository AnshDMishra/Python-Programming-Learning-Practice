s=input('enter the string:')
l=len(s)
for i in range(l):
    if (s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u'):
        print(s[i],end=' ')

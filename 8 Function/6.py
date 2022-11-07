
def arm(n):
    s=0
    nn=n
    while(n>0):
        r=n%10
        n=n//10
        s=s+(r**3)
    if (nn==s):
        print('yes armstrong')
    else:
        print('not armstrong')
i=int(input('enter no.'))
arm(i)

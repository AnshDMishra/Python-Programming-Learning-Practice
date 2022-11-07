def sumofdigits(n):
    s=0
    while(n>0):
        r=n%10
        s=s+r
        n=n//10
    return print(s)
a=int(input('enter no.'))
sumofdigits(a)
    

def reverse(n):
    rev=0
    while(n>0):
        r=n%10
        n=n//10
        rev=(rev*10)+r
    return print(rev)
i=int(input('enter no.'))
reverse(i)

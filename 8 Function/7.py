def reverse(n):
    rev=0
    nn=n
    while(n>0):
        r=n%10
        n=n//10
        rev=(rev*10)+r
    if (rev==nn
        ):
        print('yes palindrome')
    else:
        print('not palindrome')
i=int(input('enter no.'))
reverse(i)

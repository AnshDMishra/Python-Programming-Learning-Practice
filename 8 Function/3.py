def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    if c==2:
        print('no. is prime')
    else:
        print('not prime')
    return ''
a=int(input('enter no.'))
prime(a)

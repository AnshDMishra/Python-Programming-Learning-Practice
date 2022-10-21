def fab(n):
    a,b=0,1
    print(a,end=' ')
    for i in range(n-1):
        a,b=b,a+b
        print(a,end=' ')
x=int(input('enter no of terms:'))
fab(x)

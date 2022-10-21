a=int(input("enter 1st number : "))
b=int(input("enter 2nd number : "))
c=int(input("enter 3rd number : "))
if(a>=b and b>=c):
    print("1st number is greater")
elif(b>=a and a>=c):
    print("2nd number is greater")
else:
    print("3rd number is greater")

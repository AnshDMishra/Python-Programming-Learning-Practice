x=int(input("select an option :\n"
      "1. perform addition\n"
      "2. perform subtraction\n"
      "3. perform multiplication\n"
      "4. perform division\n"
      "5. perform inverse\n"
      "6. perform squaring\n"
      "7. perform cube of number\n"))
if(x==1):
    a=float(input("enter 1st number: "))
    b=float(input("enter 2nd number: "))
    print("addition is :",a+b)
elif(x==2):
    a=float(input("enter 1st number: "))
    b=float(input("enter 2nd number: "))
    print("addition is :",a-b)
elif(x==3):
    a=float(input("enter 1st number: "))
    b=float(input("enter 2nd number: "))
    print("addition is :",a*b)
elif(x==4):
    a=float(input("enter 1st number: "))
    b=float(input("enter 2nd number: "))
    print("addition is :",a/b)
elif(x==5):
    p=int(input("1. additive inverse\n"
          "2. multiplicative inverse\n"))
    if(p==1):
        a=float(input("enter number:"))
        print("Additive inverse of number is",-(a))
    if(p==2):
       a=float(input("enter number:"))
       print("Multiplicative inverse of number is :",1/a)
elif(x==6):
    a=float(input("enter number: "))
    print("Square of number is",a*a)
elif(x==7):
    a=float(input("enter number: "))
    print("cube of number is",a*a*a)
else:
    print("wrong choice")

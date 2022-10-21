x=int(input("select an option :\n"
      "1. check entered number is even or odd\n"
      "2. check entered num is postive or negative\n"))
if(x==1):
    a=float(input("enter number: "))
    if(a%2==0):
        print("number is even")
    else:
        print("number is odd")
elif(x==2):
    b=float(input("enter number: "))
    if(b>0):
        print("number is positive")
    elif(b<0):
        print("number is negative")
    else:
        print("you entered zero which is neither positive nor negative")
else:
    print("wrong choice")

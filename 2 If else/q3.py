num=int(input("enter number:"))
if(num%3==0 and num%5==0):
    print("number is divisible by 3 and 5")
elif(num%3==0):
    print("number is divisible by 3 only")
elif(num%5==0):
    print("number is divisible by 5 only")
else:
    print("not divisible by either 3 or 5")

a=int(input("enter the balance of your account\n"))
y=input('''select from following:
            enter code w for withdraw
            enter code d for deposit
            enter code c for checking balance\n''')
if(y=="w"):
    print("enter the amount you want to withdraw :\n",end=" ")
    amt=int(input())
    p=a-amt
    if(p>500):
       print("your remaining balance is \n",a-amt)
    else:
        print("SORRY!!! You don't have sifficient balance\n")
elif(y=="d"):
    amt=int(input("enter amount you want to deposit\n"))
    print("your new balance is : ",a+amt)
elif(y=="c"):
    print("your balance is: ",a)
    
else:
    print("wrong choice")

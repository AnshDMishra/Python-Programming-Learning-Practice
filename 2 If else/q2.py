cp=int(input("enter the cost price :"))
sp=int(input("enter the selling price :"))
if(sp>cp):
    print("profit :",sp-cp)
else:
    print("loss :",cp-sp)

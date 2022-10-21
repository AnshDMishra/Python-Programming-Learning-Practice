m=float(input("enter maths marks out of 100:"))
phy=float(input("enter physics marks out of 100:"))
che=float(input("enter chemistry marks out of 100:"))
if(m>=60 and phy>=50 and che>=40):
    print("qulified for admission")
elif((m+phy+che)>=200):
    print("Qualified for admission")
elif((m+phy)>=150):
    print("qualified for admission")
else:
    print("SORRY! NOT QUALIFIED")
    

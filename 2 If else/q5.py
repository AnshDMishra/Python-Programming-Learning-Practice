m=float(input("enter maths marks out of 100:"))
sci=float(input("enter science marks out of 100:"))
eng=float(input("enter english marks out of 100:"))
hin=float(input("enter hindi marks out of 100:"))
sst=float(input("enter sst marks out of 100:"))
Perc=((m+sci+eng+sst+hin)*100)/500
if(Perc>=60):
    print("first div")
elif(Perc<=59 and Perc>=50):
    print("second div")
elif(Perc<=49 and Perc>=40):
    print("third div")
else:
    print("fail")
    

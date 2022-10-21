x=int(input("""select an option :
1. find area rectangle
2. find area of circle"""))
if(x==1):
    l=float(input("enter length of rectangle"))
    w=float(input("enter breadth of rectangle"))
    print("Area of rectangle :",l*w)
elif(x==2):
    r=int(input("enter radius of circle"))
    print("Area of circle :",3.14*r*r)
else:
    print("wrong option!!")

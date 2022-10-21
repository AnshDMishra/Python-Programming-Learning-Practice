x=int(input("how many string u want to enter"))
l=[(input("enter string : ")) for i in range(x)]
#print(l)
c=0
for j in l:
    if(len(j)>=2):
        #print(j)
        if(j[0]==j[-1]):
           # print(j)
            c=c+1
print(c)

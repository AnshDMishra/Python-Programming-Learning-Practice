s=input('enter string:')
def insert(s):
    
    l=len(s)
    if(l>=3):
        a=s[:3]
        print(a,end='')
        return '';
print(insert(s))

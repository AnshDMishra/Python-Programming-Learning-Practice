s=input('enter string:')
def insert(s):
    
    l=len(s)
    if(l>=2):
        a=s[l-2:]
        for i in range(4):
            print(a,end='')
        return '';
print(insert(s))

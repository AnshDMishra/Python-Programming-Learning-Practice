d={1:2,2:3,4:5,3:7}
g={}
for k,v in sorted(d.items(),key=lambda item:item[1]):
    g[k]=v
print(g)

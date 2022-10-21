d1={1:10,2:20,3:30}
d2={1:10,5:50,6:60}
for i in d1:
    for j in d2:
        if i==j and d1[i]==d2[j]:
            print(i,':',d1[i],'present in both')

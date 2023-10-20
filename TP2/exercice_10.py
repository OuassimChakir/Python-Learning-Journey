L1 = [1,3,6,78,35,88,55]
L2 = [12,24,35,24,88,120,155]
L3 = []
print(L1)
print(L2)

if(len(L1) <= len(L2)):
    for element in L1:
        if L2.count(element) != 0 :
            L3.append(element)
else:
    for element in L2:
        if L1.count(element) != 0 :
            L3.append(element)
print(L3)

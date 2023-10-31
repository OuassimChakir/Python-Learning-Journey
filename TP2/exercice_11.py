L = [8, 24, 48, 2, 16]
# L.reverse()
print(L)
posi = 0
negi = -1
stopPoint = int(len(L) / 2)
while posi < stopPoint:
    x = L[posi]
    L[posi] = L[negi]
    L[negi] = x
    posi = posi + 1
    negi = negi - 1
print(L)
#Leetcode https://leetcode.com/problems/trapping-rain-water/description/

#height = [0,1,0,2,1,0,1,3,2,1,2,1]
#height = [4,2,0,3,2,5]
#height = [1]
#height = [5,4,1,2]
height = [5,5,1,7,1,1,5,2,7,6]
print("Algne list:", height)

uusn = []
n = -1
summa = 0
#Kui list tyhi, siis tagasta kohe 
if len(height) == 0:
    print("summa:", summa)
else:
    if height[0] < height[1]:
        for item in height:
            n += 1
            if height[n] > height[n-1] and height[n] > height[n+1]:
                uusn.append(n)
        print("Seinad: ", uusn)
    else:
        i = -1
        while n + 1 < len(height):
            for item in height:
                n += 1
                if n == 0 and height[n] > height[n+1]:
                    uusn.append(n)
                    i += 1
                    print("1. n", n)
                    print("1. lisatud arv", uusn[n])
                elif n + 1 == len(height):
                    if height[n] > height[n-1]:
                        uusn.append(n)
                        i += 1
                        print("2. n", i)
                        print("2. lisatud arv", uusn[i])
                else: 
                    if height[n] > height[n-1] and height[n] > height[n+1]:
                        if height[n] > height[uusn[i]]:
                            uusn.append(n)
                            i += 1
                            print("3. n", i)
                            print("3. lisatud arv", uusn[i])

    pikkus = len(uusn)
    jrknr = 0

    while jrknr < pikkus - 1:
        print("algus ja lõpp: (positsioon listis)", uusn[jrknr], uusn[jrknr+1])
        vahemikud = height[uusn[jrknr]:uusn[jrknr+1]]
        vahemikud.pop(0)
        print("väärtused seinte vahel", vahemikud)
        v2ikseim = min(height[uusn[jrknr]], height[uusn[jrknr+1]])
        print("väiksem sein: (väärtus)", v2ikseim)

        for mm in vahemikud:
            if v2ikseim >= mm:
                summa = summa + (v2ikseim-mm)
                print("vahesumma", summa)
        jrknr += 1
        print("--------------")

    print("summa:", summa)

    
    
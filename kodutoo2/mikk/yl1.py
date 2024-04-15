from typing import List
def maxArea(height: List[int]) -> int:

# Leetcode 11. https://leetcode.com/problems/container-with-most-water/description/ 
#You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.
    
    
#See oli mu esimen naiivne lahendus, kuid selle keerukus vähemalt O(n*n) ja leetcode testidest ei lähe läbi     
#         areaList =[]
#         for y in range (len(height)):
#             for x in range (len(height)):
#                 if y < x:
#                     shorter = min(height[y], height[x])
#                     area = (x - y)*shorter
#                     areaList.append(area)           
#         largest = max(areaList)
#         return largest


# Lahendus väiksema ajalise keerukusega
# Käin läbi selle kõrguste listi vaid ühe korra, kuid kontrollides kahte muutjat (vasak ja parem) ja leides selle läbi suurima area
    leitudMax = 0
#Muutjua vasak on selle anuma vasak külg ja seetõttu on ta algväärtus 0
    vasak = 0
    
#Muutjua parem on selle anuma parem külg ja seetõttu on ta suurus listi pikkus -1
    parem = len(height)-1
#Loop töötab kuni vasak ja parem kokku saavad
    while vasak < parem:
#min() leiab kahest arvust väiksema(sest veekõrgust mõjutab väiksem neist kahest
        shorter = min(height[vasak], height[parem])
#Pindala arvutamine (ristküliku pindala, a*b)
        area = (parem - vasak)*shorter
# Suurima ülese märkimine    
        if leitudMax < area:
            leitudMax = area
#Liigutan väiksema väärtusega muutujat edasi        
        if height[vasak] < height[parem]:
            vasak += 1
        else:
            parem -= 1
                
    return leitudMax



height =[1,8,6,2,5,4,8,3,7]
print(maxArea(height))
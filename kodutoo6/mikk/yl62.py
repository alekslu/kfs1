# https://leetcode.com/problems/valid-boomerang/
# 1037. Valid Boomerang
# 
# Given an array points where points[i] = [xi, yi] represents a point on the X-Y plane, return true if these points are a boomerang.
# 
# A boomerang is a set of three points that are all distinct and not i

def isBoomerang(points):
    k = []
    previous = points[0]
# Kontrollib et oleks eraldi punktid
    if points[0] == points[1] or points[1] == points[2] or points[0] == points[2]:
        return False
# Leiab tõusud    
    for i in points:
        if previous != i:
# Nulliga jagamise vältimiseks
            if previous[0]-i[0] == 0:
                k.append("x")
            else:
                
                t = (previous[1]-i[1])/(previous[0]-i[0])
                k.append(t)
        
        previous = i
# Kui tõusud ühtivad == sama joone peal == pole boomerang
    print(k)
    if k[0] != k[1]:
        print("true")
    else:
        print( "false")


# Funktsiooni väljakutsumine
points = [[0,0],[1,1],[1,1]]
print(isBoomerang(points))

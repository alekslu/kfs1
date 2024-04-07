from typing import List

# Ülessanne 1481 LeetCode https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals
# Ülessandeks on leida, mis on minimaalne kogus erinevaid numbreid jääb alles, kui eemaldada "k" kogus numbreid järjendist

def findLeastNumOfUniqueInts(arr: List[int], k: int) -> int:

               
#  Esmalt loen kokku mitu erinavat numbrit on esialgeses järjendis
        unikaalsed = len(set(arr))
        
# Loon sõnastiku, kus number on key ja selle korduste arv järjendis on value        
        numbrid = {}
        for a in arr: 
            if a in numbrid:
                counter = numbrid.get(a)+1
                numbrid.update({a : counter})             
                        
            else:
                numbrid[a] = 1
                
                
# Sorteerin sõnastiku valuede järgi, väiksemad eespool              
# https://stackoverflow.com/a/613218
        sorditud = dict(sorted(numbrid.items(), key=lambda item: item[1]))
# käin läbi sorditud sõnastiku, eemaldades vähimad arvud esimesena
        for b in sorditud:

            if k >= sorditud.get(b):
# Lahutan unikaalsete arvude summast 1, kui arvu saab eemaldada
                unikaalsed -= 1
# Lahutan kordajast k selle, kui suure koguse ma eemaldasin                 
                k -= sorditud.get(b)
            
        return(unikaalsed)


# Näidis
array = [4,3,1,1,3,3,2]
n = 3    
print(findLeastNumOfUniqueInts(array, n))


     

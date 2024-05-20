# Function to convert decimal number
# to binary using recursion

# https://leetcode.com/problems/sum-of-all-subset-xor-totals/description/?envType=daily-question&envId=2024-05-20

# https://stackoverflow.com/questions/1482308/how-to-get-all-subsets-of-a-set-powerset
# Leian alamhulgad
def FindSubsets(arr):
    subsets = []
    x = len(arr)
    for i in range(1 << x):
        subsets.append([arr[j] for j in range(x) if (i & (1 << j))])
        
# Tühja setti pole vaja, selle otsitav väärtus on 0    
    subsets.pop(0)    
    return subsets
    
    

subsets = FindSubsets([3,4,5,6,7,8])
sum = 0
subsum = 0
for i in subsets:   
#   Ühekohalised
    if len(i) == 1:
        sum+= 0^i[0]
        
# Mitmekohalised        
    else:
        for j in i:
            subsum ^= j
#             print(subsum)
        
        sum +=subsum
        subsum = 0

print(sum)        
         



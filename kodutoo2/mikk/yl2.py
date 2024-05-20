# Leetcoode 728. https://leetcode.com/problems/self-dividing-numbers
# A self-dividing number is a number that is divisible by every digit it contains.
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# A self-dividing number is not allowed to contain the digit zero.
# Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].

# Jagumise kontrollimise funktsioon
def jagumiseKontroll (number):
#Loob järjendi arvud[], milles on arvud millest number koosneb 
    arvud = [*map(int,str(number))]
    for x in arvud:
        if x == 0:
            return False
#Kontroll, kas number jagub kõiki enda arvudega
        elif number % x != 0:            
            return False        
    return True
    

left = 47
right = 85

x = left
jaguvadNumbrid = []

# Käib läbi vahemiku left ja right vahel, kontrollib igat numbrit
while x <= right:
    if jagumiseKontroll(x) == True:
        jaguvadNumbrid.append(x)    
    x +=1
    
    
print(jaguvadNumbrid)
    
    
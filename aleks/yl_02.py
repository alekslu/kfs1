# Leetcode https://leetcode.com/problems/find-the-winner-of-an-array-game/
# Veidi aeglane võrreldes teiste lahendustega leetcodeis, aga võttis mul päris mitu lahendust aega
# Sisuliselt võrreldakse listis esimest kahte elementi ning väikseim neist lisatakse listi lõppu. Kui 
# element on k (muutuja) korda võita ehk olla suurim element kahe esimese seas, siis lõpeb võrdlemine ja leitakse võitja

#arr = [1,11,22,33,44,55,66,77,88,99]
#k = 1000000000

arr = [1,25,35,42,68,70]
k = 2

total_wins = 0
last_winner = 0

if k > len(arr):
    print(max(arr))

if k == 1:
    if arr[0] > arr[1]:
            arr.append(arr.pop(1))
    else:
        arr.append(arr.pop(0))
else:
    while total_wins < k:
        winner = max(arr[0], arr[1])
        if last_winner != winner:
            total_wins = 0

        print(arr)

        if winner == arr[0]:
            arr.append(arr.pop(1))
        else:
            arr.append(arr.pop(0))
        
        last_winner = winner
        total_wins += 1        
        
        print("last winner:", last_winner, "v6ite:", total_wins)

print("Võitja:", arr[0])



''' 
Leetcode keskkonda kopeerimiseks::

class Solution(object):
    def getWinner(self, arr, k):
        total_wins = 0
        last_winner = 0

        if k > len(arr):
            return max(arr)

        if k == 1:
            if arr[0] > arr[1]:
                    arr.append(arr.pop(1))
            else:
                arr.append(arr.pop(0))
        else:
            while total_wins < k:
                winner = max(arr[0], arr[1])
                if last_winner != winner:
                    total_wins = 0

                if winner == arr[0]:
                    arr.append(arr.pop(1))
                else:
                    arr.append(arr.pop(0))
                
                last_winner = winner
                total_wins += 1

        return arr[0]
'''
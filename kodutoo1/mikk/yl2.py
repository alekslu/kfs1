# Leetcode 2073 https://leetcode.com/problems/time-needed-to-buy-tickets

# There are n people in a line queuing to buy tickets, where the 0th person is at the front of the line and the (n - 1)th person is at the back of the line.
# You are given a 0-indexed integer array tickets of length n where the number of tickets that the ith person would like to buy is tickets[i].
# Each person takes exactly 1 second to buy a ticket. A person can only buy 1 ticket at a time and has to go back to the end of the line (which happens instantaneously) in order to buy more tickets. If a person does not have any tickets left to buy, the person will leave the line.
# Return the time taken for the person at position k (0-indexed) to finish buying tickets.

tickets = [84,49,5,24,70,77,87,8]
k = 3

#Muutja timer loeb kokku palju aega kulub ja on asi mida me otsime
#Kuna k-ndal inimesel on vaja osta kõik enda piletid nagunii, võib selle juba alguses  timerisse sisse lugeda
timer = tickets[k]

# Käin kogu järjekorra läbi
for i in range(len(tickets)):
#     Kui inimene on eespool kui k, siis kulub tal maksimaalselt sama palju aega piletite ostmiseks kui k-l
    if i < k:
#         Kui ta ostab vähem või sama palju kui k, pileteid, siis läheb see timer-isse
        if tickets[i] <= tickets[k]:
            timer += tickets[i]
#             Kui ta ostab rohkem piletid läheb timerisse k piletite kogus
        else:
            timer += tickets[k]
# Kui inimene on k-st taga pool             
    elif i > k:
#         Kui ta ostab vähem pileteid kui k, siis läheb see timer-isse
        if tickets[i] < tickets[k]:
            timer += tickets[i]
#             Kui ta ostab rohkem kui k, siis läheb arvesse k piletid -1, sest kui k-l saavad piletid ostetud, on ülesanne sooritatud
        else:
            timer += (tickets[k]-1)
            
print(timer)    
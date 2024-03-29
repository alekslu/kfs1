
# x arvu kollast palli ja y arvu sinist palli
inventory = [1000000000]
#inimene tahab saada k amount palle
orders = 1000000000

def bubbleSort(inventory):
    n = len(inventory)
    for i in range(n-1):
        for j in range(0, n-1-i):
            if inventory[j] > inventory[j+1]:
                inventory[j], inventory[j+1] = inventory[j+1], inventory[j]

    return inventory

def maxProfit(inventory, orders):
    profit = 0
    while orders > 0:
        i = inventory.index(max(inventory))
        if inventory[-1] >= inventory[i]:
            profit += inventory[-1]
            orders -= 1
            inventory[-1] -= 1
        elif inventory[-1] < inventory[i]:
            profit += inventory[i]
            orders -= 1
            inventory[i] -= 1

    return profit


m = bubbleSort(inventory)
print(m)
print(maxProfit(m, orders))
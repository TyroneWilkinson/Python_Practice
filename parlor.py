# https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=search

def whatFlavors(cost,money):
    """
    Determine the two ice cream flavors that must be purchased during a
    trip to the parlor. The flavors are denoted by their costs. The ID 
    numbers for the cost of each flavor are the 1-based index numbers of 
    the integer list. All the money must be spent during each trip.

    Parameters:
    cost (list): An integer list representing the prices for the flavors.
    money (integer): The amount of money that must be spent.

    Returns:
    2 selected ID numbers are printed smallest to largest separated by a 
    space.  
    """
    costs = sorted(c for c in cost if c < money)
    i = 0
    j = -1
    while True:
        if costs[i]+costs[j]==money: break
        if costs[i]+costs[j]>money: j-=1
        if costs[i]+costs[j]<money: i+=1
    print("Costs: ",costs[i],costs[j])
    first = cost.index(costs[i])+1
    if costs[i] == costs[j]:
        print(first, cost.index(costs[j],first)+1)
        return
    print(*sorted([first, cost.index(costs[j])+1]))
# whatFlavors([7,2,5,4,11],12)
t = int(input()) # trips to the parlor
for _ in range(t):
    money = int(input())
    n = int(input()) # length of 'cost'
    cost = [int(x) for x in input().split()]
    whatFlavors(cost,money)

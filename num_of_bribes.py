# https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=arrays

# Utilized modified bubble sort for this method

def minimumBribes(a):
    """
    Determine the minimum number of swaps necessary to transform an ordered
    list into list q. Each element is allowed to swap at most 2 times.

    This method utilizes modified bubble sort.

    Modified bubble sort includes a flag that is set if an exchange is made
    after an entire pass over the array. If no exchange is made, then it 
    should be clear that the array is already in order because no two 
    elements need to be switched. In that case, the sort should end. The 
    new best case order for this algorithm is O(n), as if the array is 
    already sorted, then no exchanges are made.
    https://www.cprogramming.com/tutorial/computersciencetheory/sorting1.html

    Parameters:
    a (list): An integer list after the swaps.

    Returns:
    Prints the minimum number of swaps or "Too chaotic" if an element has 
    swapped positions more than twice.
    """
    flag = 1
    n = len(a)
    swap_dict = {}
    for i in range(n):
        if flag == 1:
            flag = -1
            for j in range(n-1):
                if a[j] > a[j+1]:
                    flag = 1
                    a[j], a[j+1] = a[j+1], a[j]
                    if a[j+1] in swap_dict:
                        swap_dict[a[j+1]] += 1
                        if swap_dict[a[j+1]] > 2:
                            print("Too chaotic")
                            return
                    else:
                        swap_dict[a[j+1]] = 1
    print(sum(swap_dict.values()))

t = int(input()) # Number of test cases
for _ in range(t):
    n = int(input()) # Length of list q
    q = [int(x) for x in input().split()]
    minimumBribes(q)
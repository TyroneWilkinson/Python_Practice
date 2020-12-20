def countSwaps(a):
    """
    Determines the minimum number of conditional checks taking place in
    Bubble sort.

    Parameters:
    a (list): The integer list to be sorted.

    Returns:
    3 Lines are printed:
    1. "Array is sorted in 'i' swaps.", where 'i' is the number of swaps that
        took place.
    2. "First Element: 'f'", where 'f' is the first element in the sorted list.
    3. "Last Element: 'l'", where 'l' is the last element in the sorted list.
    """
    n = len(a)
    swaps = 0
    for i in range(n):
        for j in range(n-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swaps += 1
    print(f"Array is sorted in {swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")

n = int(input())
a = [int(x) for x in input().split()]
countSwaps(a)
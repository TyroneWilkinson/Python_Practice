
def getMoneySpent(keyboard, drives, b):
    """
    Determines the most expensive computer keyboard and USB drive that can
    be purchased with a given budget.

    Parameters:
    keyboard (list): A list of integers denoting the keyboard prices.
    drives (list): A list of integers denoting the drive prices.
    b (integer): The budget.

    Returns:
    integer: The maximum that can be spent or -1 if it's not possible to
        buy both items.
    """
    # k = [x for x in keyboard if x < b]
    # d = [x for x in drives if x < b]

    # try:
    #     return max([k_+d_ for k_ in k for d_ in d if k_+d_ <= b])
    # except ValueError: 
    #     return -1
    return max([k+d for k in keyboard for d in drives if k+d <= b] + [-1])

b, n, m = map(int, input().split())
keyboard = list(map(int, input().split()))
drives = list(map(int, input().split()))

print(getMoneySpent(keyboard, drives, b))
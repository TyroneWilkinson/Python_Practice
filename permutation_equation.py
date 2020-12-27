def permutationEquation(p):
    """
    Given a sequence of n integers, p(1),p(2),...,p(n) where each element
    is distinct and satisfies 1 <= p(x) <= n. For each x where 1 <= x <= n,
    find any integer y such that p(p(y)) ≡ x and print the value of y on a
    new line.

    Parameters:
    p (list): An integer list.

    Returns:
    Prints the value of y on a new line.
    """
    for i in range(1,len(p)+1):
        print(p.index(p.index(i)+1)+1)
        
n = int(input()) # The number of elements in the sequence.
p = [int(x) for x in input().split()]
permutationEquation(p)
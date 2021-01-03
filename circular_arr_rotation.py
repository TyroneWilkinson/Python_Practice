# https://www.hackerrank.com/challenges/circular-array-rotation/problem

def circularArrayRotation(arr,k,queries):
    """
    Prints elements in certain indices in a list after 'k' right 
    circular rotation operations.

    Parameters:
    arr (list): The integer list to rotate.
    k (integer): The rotation count.
    queries (list): The indices to report.

    Returns:
    list: The elements at the requested indices. 
    """
    return [(arr[-(k%len(arr)):]+arr[:-(k%len(arr))])[i] for i in queries]
    
    
# a = # of elements in arr; k = Rotation count; q = # of queries
a, k, q = map(int, input().split())
arr = [int(x) for x in input().split()]
queries = [int(input()) for _ in range(q)]
    
print(circularArrayRotation(arr,k,queries))
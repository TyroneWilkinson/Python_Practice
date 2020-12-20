# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms
def minimumAbsoluteDifference(arr):
    """
    Determines the minimum absolute difference between any two elements in
    a list of integers.

    Parameters:
    arr (list): A  list of integers whose length >= 2.

    Returns:
    integer: The minimum absolute difference found.
    """
    arr.sort(key=abs)
    return min(abs(arr[i]-arr[i+1]) for i in range(len(arr)-1))

    # mins = []
    # n = len(arr)
    # for i in range(0,n-1):
    #     for j in range(i+1,n):
    #         mins.append(abs(arr[i]-arr[j]))
    # return min(mins)
    # return min([abs(arr[i]-arr[j]) for i in range(0,len(arr)-1) for j in range(i+1,len(arr))])

n = int(input())
arr = list(map(int, input().split()))
print(minimumAbsoluteDifference(arr))


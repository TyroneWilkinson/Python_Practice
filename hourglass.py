# https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

def hourglassSum(arr):
    """
    Calculates the hourglass sum for every hourglass in a 1-by-6 list then 
    print the maximum hourglass. There are 16 hourglasses in total.
    
    Parameters:
    arr (list): A 1-by-6 list representing a 6x6 matrix with the hourglass 
        being 3x3.
    
    Returns:
    integer: The maximum hourglass sum.
    """
    sums = []
    for i in range(4):
        for j in range(4):
            sums.append(sum(arr[i][j:j+3]+[arr[i+1][j+1]]+arr[i+2][j:j+3]))
    return max(sums)

arr = []
for _ in range(6):
    arr.append(list(map(int, input().split())))
print(hourglassSum(arr))
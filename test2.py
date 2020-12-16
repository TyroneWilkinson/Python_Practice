def longestSubarray(arr):
    """
    Determines the length of the longest sublist in an integer list that
    contains no more than two distinct values such that the distinct values
    differ by no more than 1.
    
    Parameters:
    arr (list): An integer list.
    
    Returns:
    integer: The length of the longest sublist.
    """
 
    count = 0
    counts = []
    arr_size = len(arr)
    for i in range(0, arr_size-1):
        lst = []
        counts.append(count)
        count = 0
        for j in range(i+1, arr_size):
            lst.append(arr[i])
            lst.append(arr[j])
            if abs(arr[i]-arr[j]) < 2 and len(set(lst)) < 3:
                count += 1
            else:
                break
    if counts==[]: return 1
    return max(counts)+1

print(longestSubarray([2, 2, 1]))
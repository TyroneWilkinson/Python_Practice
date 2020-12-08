
def countingValleys(steps,path):
    """
    Determines the number of valleys walked through given a sequence of up 
    and down steps.

    Parameters:
    steps (integer): The number of steps taken.
    path (string): The types of steps taken.

    Returns:
    integer: The number of valleys traversed.
    """
    int_path = [1 if char=="U" else -1 for char in path]
    elevation = valleys = 0
    for i in int_path:
        if elevation==0 and i < 0:
            valleys += 1
        elevation += i
    return valleys


steps = int(input())
path = input().strip()
print(countingValleys(steps,path))
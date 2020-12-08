# A better solution...
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
    elevation = valleys = 0
    for step in path:
        elevation += 1 if step == "U" else -1
        valleys += elevation == 0 and step == "U"
    return valleys


steps = int(input())
path = input().strip()
print(countingValleys(steps,path))
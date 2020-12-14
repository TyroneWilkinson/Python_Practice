# I did get a weird error with my initial solution...

def hurdleRace(k,height):
    """
    Determines whether the player can jump all of the hurdles.

    Parameters:
    k (integer): The height the character can jump naturally.
    height (list): A list of integers representing the heights of the hurdles.

    Returns:
    integer: An integer denoting how much higher the player would need to jump
        to clear the highest hurdle, or 0 if the player can clear all hurdles.
    """
    # return max(height)-k if max(height)-k > 0 else 0
    return max(max(height)-k, 0)

n,k = map(int, input().split())
height = map(int, input().split())
print(hurdleRace(k,height))


def catAndMouse(x, y, z):
    """
    Determines whether cat A or B will reach the mouse or if the mouse will
    escape.

    Parameters:
    x (integer): The position of cat A.
    y (integer): The position of cat B.
    z (integer): The position of mouse C.

    Returns:
    string: "Cat A" or "Cat B" if one of them reaches the mouse first. Else
        "Mouse C" will escape if they both reach together and fight.
    """
    return "Cat A" if abs(x-z) < abs(y-z) else "Cat B" if abs(x-z) > abs(y-z) \
           else "Mouse C"

q = int(input())
for _ in range(q):
    x, y, z = map(int, input().split())
    print(catAndMouse(x, y, z))

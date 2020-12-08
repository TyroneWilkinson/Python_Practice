# A better solution
def pageCount(n,p):
    """
    Determines the minimum number of pages that must be turned in order to
    arrive at page p. When they open the book, page 1 is always on the right
    side.

    Parameters:
    n (integer): The number of pages in the book.
    p (integer): The page number to turn to.

    Returns:
    integer: The minimum number of pages to turn.
    """
    # Below are the number of pages starting from both ends of the book.
    return min(p//2, n//2-p//2)

n = int(input())
p = int(input())

print(pageCount(n,p))
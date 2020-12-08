
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
    start = p//2
    end = (n-p)//2 if not (n-p == 1 and n%2==0) else 1
    return start if start < end else end

n = int(input())
p = int(input())

print(pageCount(n,p))
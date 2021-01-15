# https://www.hackerrank.com/challenges/library-fine/problem

def libraryFine(d1, m1, y1, d2, m2, y2):
    """
    Given the expected and actual return dates for a library book, create 
    a program that calculates the fine (if any).

    Fee Structure:
    - fine = 0, if the book is returned on or before the due date.
    - fine = 15 * days_late if the book is returned after the due date but
      within the same month.
    - fine = 500 * months_late if the book is returned after the return 
      month but within the same year.
    - fine = 10000 if the book is returned after the return year.

    Parameters:
    d1 (integer): Returned day.
    m1 (integer): Returned month.
    y1 (integer): Returned year.

    d2 (integer): Due day.
    m2 (integer): Due month.
    y2 (integer): Due year.

    Returns:
    integer: The amount of the fine.
    """
    if y1 > y2: return 10000

    if y1 == y2 and m1 > m2: return 500*(m1-m2)

    if y1 == y2 and m1 == m2 and d1 > d2: return 15*(d1-d2)

    return 0

d1, m1, y1 = map(int, input().split())
d2, m2, y2 = map(int, input().split())

print(libraryFine(d1, m1, y1, d2, m2, y2))


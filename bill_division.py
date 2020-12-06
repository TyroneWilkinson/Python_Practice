
def bonAppetit(bill, k, b):
    """
    Determines whether the bill was properly split between Anna and Brian.
    
    Parameters:
    bill (list): A list of integers representing the cost of each item 
        ordered.
    k (integer): An integer representing the zero-based index of the item
        Anna doesn't eat.
    b (integer): An integer denoting the amount of money Anna contributed 
        to the bill.

    Returns:
    string: "Bon Appetit" if the bill is fairly split.
        or
    integer: The integer amount of money that Brian owes Anna.
    """
    anna = (sum(bill) - bill[k])//2
    print("Bon Appetit") if anna == b else print(b-anna)

n, k = list(map(int, input().split()))
bill = list(map(int, input().split()))
b = int(input())

bonAppetit(bill,k,b)
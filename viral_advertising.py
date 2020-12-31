# https://www.hackerrank.com/challenges/strange-advertising/problem

def viralAdvertising(n):
    """
    Determines the amount of people who have "liked" an ad by the end of a
    given day.

    At the start of the first day the ad is shown to 5 people. Half of them
    like the advertisement who each then share it with 3 of their friends 
    the following day. This pattern continues.

    Parameters:
    n (int): The day number.

    Returns:
    integer: The cumulative likes at that day.
    """
    liked = [5//2]*(n+1) # first day likes

    for i in range(n):
        liked[i+1]=liked[i]+liked[i]//2 # populate list with n-day likes (plus 1)

    return sum(liked[:n])

# Another solution I found
def viralAdvertising2(n):
    m = [2]
    for i in range(n-1):
        m.append(int(3*m[i]/2))
    return sum(m)


print(viralAdvertising(int(input())))
print(viralAdvertising2(int(input())))

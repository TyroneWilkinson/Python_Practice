# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
# A cool solution I found.
def climbingLeaderboard(l, p):
    """
    Determine a player's ranking after each game played given his scores
    and the leaderboard scores.

    Note: The game uses dense ranking.

    Parameters:
    l (list): An integer list representing the leaderboard scores.
    p (list): An integer list representing the player's scores.
    
    Returns:
    list: An integer list representing the player's ranking after each score.
    """
    l = sorted(set(l),reverse=True)
    n = len(l)
    for i in p:
        while (n > 0) and (i >= l[n-1]):
            n -= 1
        print(n+1)

input()
leaderboard = [int(x) for x in input().split()]
input()
player = [int(x) for x in input().split()]
climbingLeaderboard(leaderboard,player)

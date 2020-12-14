# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
# Not fast enough.
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
    ranks = []
    l = sorted(list(set(l)), reverse=True)
    for ele in p:
        if ele not in l: 
            l.append(ele); l.sort(reverse=True) # Avoids duplicates and reorders
        ranks.append(l.index(ele) + 1) # Ranking starts with "1" not "0"
    return ranks
    

input()
leaderboard = [int(x) for x in input().split()]
input()
player = [int(x) for x in input().split()]
print(climbingLeaderboard(leaderboard,player))
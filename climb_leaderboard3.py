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
    #[sorted(list(set(l+p[:i+1])), reverse=True).index(j)+1 for i,j in enumerate(p)] 
    ranks = []
    l = sorted(list(set(l)), reverse=True)
    for score in p:
        if score < min(l):
            ranks.append(l.index(min(l))+2)
            continue
        for rank in l:
            if rank <= score:
                ranks.append(l.index(rank)+1)
                break
    return ranks

input()
leaderboard = [int(x) for x in input().split()]
input()
player = [int(x) for x in input().split()]
print(climbingLeaderboard(leaderboard,player))
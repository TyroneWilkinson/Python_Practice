
def formingMagicSquare(s):
    """
    Converts a 3x3 matrix to a magic square at minimal cost.

    Parameters:
    s (list): A 1x3 list of integer lists representing a 3x3 matrix.

    Return:
    integer: The minimal cost to convert the 3x3 matrix into a magic square.
    """
    # Every possible variation of a 3x3 magic square.
    # There are 4 rotations and for mirror images of said rotations.
    orig = [[8,1,6],[3,5,7],[4,9,2]]        
    switchd = orig[::-1]                    # [[4,9,2],[3,5,7],[8,1,6]]
    reversd = [i[::-1] for i in orig]       # [[6, 1, 8], [7, 5, 3], [2, 9, 4]]
    switchrev = [i[::-1] for i in switchd]  # [[2, 9, 4], [7, 5, 3], [6, 1, 8]]
    transp = [[8,3,4],[1,5,9],[6,7,2]]      
    t_switchd = transp[::-1]                # [[6, 7, 2], [1, 5, 9], [8, 3, 4]]
    t_reversd = [i[::-1] for i in transp]   # [[4, 3, 8], [9, 5, 1], [2, 7, 6]]
    t_switchrev = [i[::-1] for i in t_switchd]  # [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
  
    check_list = [orig,switchd,reversd,switchrev,transp,t_switchd,t_reversd,t_switchrev]
    costs = [[],[],[]]

    for ind, ele in enumerate(s):
        for test in check_list:
            costs[ind].append(sum([abs(x-y) for x,y in zip(ele,test[ind])]))

    tot_costs = [(a,b,c) for a,b,c in zip(*costs)]
    return min([sum(cost) for cost in tot_costs])    

s = [(list(map(int,input().split()))) for _ in range(3)]
print(formingMagicSquare(s))
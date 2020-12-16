
from collections import Counter
def nearlySimilarRectangles(sides):
    """
    Given a list of rectangles with the lengths of their sides, calculate
    the number of pairs of nearly similar rectangles in the array.
    
    Two Rectangles with sides (a,b) and (c,d) are nearly similar if 
    a/c == b/d.
    
    Parameters:
    sides (list): A 2D list of integer pairs, each representing the sides of
    a rectangle.
    
    Returns:
    integer: The number of nearly similar rectangles in the 2D list.    
    """
    # arr_size = len(sides)
    # count = 0
    # for i in range(0, arr_size-1):
    
    #     for j in range(i+1, arr_size):
    #         if sides[i][0]/sides[j][0] == sides[i][1]/sides[j][1]:
    #             count +=1
    # return count

    rects = [x[0]/x[1] for x in sides]  
    return sum([i for i in Counter(rects).values() if i > 1])
    # maxi = rects.count(Counter(rects).most_common(1)[0][0])
    # return maxi if maxi > 1 else 0

    # listA = [45, 20, 11, 50, 17, 45, 50,13, 45]
    # print("Given List:\n",listA)
    # occurence_count = Counter(listA)
    # res=occurence_count.most_common(1)[0][0]
    
    # rects = [x[0]/x[1] for x in sides]  
    # # maxi = rects.count(max(set(rects), key=rects.count))
    # # return maxi if maxi > 1 else 0
    # try:
    #     return rects.count(mode(rects))
    # except StatisticsError:
    #     return 0

print(nearlySimilarRectangles([[4,5],[25,50]]))
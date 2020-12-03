def breaking_records(score):
    """
    Determines the number of times a record is broken for most and least 
    points scored during a season.

    Parameters:
    scores (list): A list of integers representing the points scored in 
        one season.

    Returns:
    integers: Two integers denoting the number of times the max and min 
        points records were broken.
    """
    min = max = score[0]
    min_count = max_count = 0
    for i in score[1:]:
        if i > max:
            max_count += 1
            max = i
        if i < min:
            min_count += 1
            min = i
    return max_count, min_count


n = int(input())
score = list(map(int, input().split()))
print(*breaking_records(score))
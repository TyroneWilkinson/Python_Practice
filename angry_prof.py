# https://www.hackerrank.com/challenges/angry-professor/problem

def angryProfessor(k, a):
    """
    Given the arrival time of each student and a threshhold number of
    attendees, determine if the class is cancelled.

    Note: 
    Arrival times <= 0 are early or on time.
    Arrival times > 0 are late.

    Parameters:
    k (integer): The threshold number of students.
    a (list): An integer list housing student arrival times.
    
    Returns:
    string: "YES" or "NO" if the class is cancelled or not.
    """
    return "YES" if len([s for s in a if s < 1]) < k else "NO"

# t = int(input()) # Number of test cases
# for _ in range(t):
#     n, k = map(int, input().split()) # Number of students and threshold
#     a = [int(x) for x in input().split()] # Student arrival times
#     print(angryProfessor(k,a))

############################################################

for _ in range(int(input())):
    n, k = map(int, input().split()) # Number of students and threshold
    print("YES") if len([s for s in input().split() if int(s) < 1]) < k else print("NO")



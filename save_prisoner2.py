# https://www.hackerrank.com/challenges/save-the-prisoner/problem
# A MUCH CLEANER SOLUTION!!!
"""
The S-1 translates the prisoner id to an equivalent index 
(since % effectively deals with indexes like 0..N-1). 
The M-1 handles the fact that the first prisoner to get a sweet is 
not counted when giving away sweets. 
Example, if you are giving away 1 sweet and you start at 
prisoner 37, it is 37 = (37 + 1 - 1) that should be warned. If you are 
giving away 2 sweets it is 38 = (37 + 2 - 1) that should be warned. 
And so on. 
The % N handles the wrapping around based on the index of the prisoners. 
And the + 1 brings us back to dealing with prisoner ID's instead of indicies.
"""

T = int(input().strip())
for _ in range(T):
    N,M,S = list(map(int, input().strip().split()))
    print(((S - 1 + M - 1) % N) + 1)

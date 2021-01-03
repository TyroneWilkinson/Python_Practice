
# I found a more efficient solution.

"""
Instead of making changes to our original array we subtract the value of 
k from m. This gives us the correct index of our required value.
"""

n,k,q = map(int,input().split())
k = k%n
a = list(map(int,input().split()))
for _ in range(q):
    m = int(input())
    print(a[m-k])
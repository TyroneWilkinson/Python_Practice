#https://www.hackerrank.com/challenges/picking-numbers/problem
# Another way of solving this using Counter (a dict subclass)
from collections import Counter
def pickingNumbers(a):
    # a = Counter(a)
    # maxi = 0
    # for k in sorted(a):
    #     print("a[k]: ", a[k])
    #     print("a.get(k+1,0): ", a.get(k+1,0))
    #     m = a[k]+a.get(k+1,0)
    #     print("a[k]+a.get(k+1,0): ", m)
    #     if maxi<m:
    #         maxi=m
    # return maxi
    a = Counter(a)
    return max(a[k]+a.get(k+1,0) for k in sorted(a))

input()
a = map(int,input().split())
print(pickingNumbers(a))
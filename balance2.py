# https://www.hackerrank.com/challenges/balanced-brackets/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues
# 2 other interesting solutions I found:

"""
Determines whether a string containing 3 types of brackets is balanced.

A sequence of brackets is balanced if:
-It contains no unmatched brackets.
-The subset of brackets enclosed within the confines of an matched pair
    of brackets is also an matched pair of brackets.

Parameters:
s (string): A string of brackets.

Returns:
string: "YES" if the sequence is balanced or "NO" if it is not.
"""
# def isBalanced1(s):
#     restart=True
#     while restart:
#         if '{}' in s:
#             s=s.replace('{}','')
#         elif '()' in s:
#             s=s.replace('()','')
#         elif '[]' in s:
#             s=s.replace('[]','')
#         else:
#             restart=False
#     return 'YES' if len(s)==0 else 'NO'

# n = int(input()) # The number of strings
# with open('temp.txt', 'w+') as f:
#     for _ in range(n):
#         s = input().strip()
#         print(isBalanced(s))

############################################################################

table =  { ')': '(', ']':'[', '}':'{' }

for _ in range(int(input())):
    stack = []
    for x in input():
        print(stack)
        if stack and table.get(x) == stack[-1]:
            stack.pop()
        else:
            stack.append(x)
    print("NO" if stack else "YES")
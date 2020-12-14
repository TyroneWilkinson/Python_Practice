# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
# 

def designerPdfViewer(h, word):
    """
    Determine the area of the rectangle highlight of a word given the 
    letters, a list of character heights, and that all letters are 1mm
    wide.

    We are only working with English lowercase letters.

    Parameters:
    h (list): A list of integers denoting the heights of each letter.
    word (string): The word to find the area of.

    Returns:
    integer: The size of the highlighted area.
    """
    # ord('a') --> ord('z'): 97 --> 122
    return len(word) * max([h[ord(char)-97] for char in word])

h = list(map(int,input().split()))
word = input().strip() # [h[ord(char)-ord('a')] for char in input()]
print(designerPdfViewer(h,word)) # max(word)*len(word)



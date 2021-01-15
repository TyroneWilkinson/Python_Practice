# https://www.hackerrank.com/challenges/sherlock-and-squares/problem

def squares(a,b):
    """
    Determine the number of square numbers between the inclusive range
    from a to b.

    Method: Calculate the square roots of a and b. The numbers between 
    those roots are the number of squares. I subract 1 from a in case 
    both happen to be squares themselves, which would give 1 less number.

    Parameters:
    a (integer): The lower range boundary.
    b (integer): The upper range boundary.

    Returns:
    integer: The number of square integers in the range.
    """
    # if a % 2 != 0: a += 1
    # if b% 2 != 0: b += 1
    # return sum(1 for i in range(a,b+1) if (i**.5).is_integer())

    return int(b**.5) - int((a-1)**.5) 

for _ in range(int(input())):
    a, b = map(int,input().split())
    print(squares(a,b))

"""
A lengthy explanation I found
Thanks to everyone who explained the fast solution. 
I'd like to explain my understanding of it for people who are not grasping 
how it works. I hope by typing it out I fix in my own mind how to think 
about problems like this, and explain longhand to others how it works in 
case the shorthand others are giving isn't clicking with you. Of course 
this supposes my understadning is correct.

The solution for this problem will be the count of a quantity of integers 
which are square numbers and have integer square roots. The trick is to not 
look at the (potentially millions large) range of values we want to examine 
to see if they are square roots, but to look at the roots they become.

So if you look at the range of all integers,

1 2 3 4 5 6 7 8 9 .... etc,

each of these can be squared to produce a value. Each maps to a 
'seemingly random' set of numbers

1 4 9 16 25 36 49 64 81 ... etc

If you had been given the values 20 and 55, and asked to find all the squares 
in between, you might iterate 20 - 55 and find the sqrt of each number, that's 
36 tests adding to the accumulated value each time you find a match.

But, each of the square roots you find in that range will be in a sequence. 
You will find

sqrt(25) = 5 sqrt(36) = 6 sqrt(49) = 7

for ANY test like this, the results MUST be the squares of a sequence of 
integers. You can't find the squares of 5,6,8, and 9 in your solution 
without the square of 7 also being in there. It has to be because you are 
looking at all numbers in a range.

So, if you find the square roots of your start and end values, that will 
give you a start and end of this range of integers which provide the 
squared values in your required range.

In the example I give here, sqrt(20) is between 4 and 5; sqrt(55) is 
between 7 and 8.

1 2 3 4 * 5 6 7 * 8 9

So in between those, there are 3 values which if you square them will be 
the 3 square numbers between 20 and 55. Your answer is 3.

This works for every range. So even if you have a billion values in your 
range, by finding their square roots you find the integers those square 
roots "surround" and therefore your required result. This is clearly a 
lot faster than checking each one or trying to create a database of all 
primes for lookup, or any other method. Find the square root of the two 
provided values and work it from there.
"""
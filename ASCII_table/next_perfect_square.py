# A perfect square is an integer ,the square root of which is also an integer.
import math
def next_perfect_square(num):
    return (math.sqrt(num) ** 2) if math.sqrt(num) % 1 == 0  else "Not a perfect square  itself." 

next_perfect_square(4)
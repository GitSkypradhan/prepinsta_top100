# A perfect square is an integer ,the square root of which is also an integer.
import math
def next_perfect_square(num):
    print(int(math.sqrt(num)+1)**2) if math.sqrt(num) % 1 == 0 else print("number itself is not perfect square.")   

next_perfect_square(4)

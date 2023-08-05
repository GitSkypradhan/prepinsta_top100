#
def sum_of_nnum(num):
    i = 1
    sum = 0
    while i <= num:
        sum = sum + i
        i +=1
    return sum

num = int(input("Enter any number: "))
print(f"Sum of natural numbers till {num} is: {sum_of_nnum(num)}")


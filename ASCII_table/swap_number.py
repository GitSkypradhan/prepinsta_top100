# using a temporary value

a = int(input("Enter number a: "))
b = int(input("Enter number b: "))

def swap_num(a,b):
    temp = b
    b = a
    a = temp
    return f"(swap number a:{a} & b:{b} )"

ans = swap_num(a,b)
print(ans)

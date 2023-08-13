def check_prime_num(num):
    for i in range(2, num):
        if i % num == 0:
            print(i,"its a prime number")
        else:
            print(i,"its not a prime number")




check_prime_num(9)
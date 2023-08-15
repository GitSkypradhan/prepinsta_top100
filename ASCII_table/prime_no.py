def check_prime_num(num):
    if num == 1: # check for 1 in input 
         print(num,"is not prime nor a composite number") 
    else: 
        for i in range(2, num): # iterate  from 2 to nearest number of given input
            if num % i == 0: # if num is compeletly divisible by 
                 print(num,'is not a prime number.')
                 break
            
        else:
            print(num,"is a prime number.")

            
num = int(input("Enter a postive num:"))
check_prime_num(num)
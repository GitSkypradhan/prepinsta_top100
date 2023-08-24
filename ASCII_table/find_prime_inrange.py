 
low_limit,high_limit = input('Enter number to (start,end): ').split(',')
prime = []

for num in range(int(low_limit),int(high_limit)+1):
    if num < 0:
        continue
    if num == 2:
        prime.append(num)
    for i in range(2,num):
        if num % i == 0:
            break
    else:
        if num not in prime:
            prime.append(num)

print(prime)

            

            




        

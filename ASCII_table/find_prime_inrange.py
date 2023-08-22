 
low_limit,high_limit = input('Enter number to (start,end): ').split(',')
prime = []

for i in range(int(low_limit),int(high_limit)):
    for j in range(2,i):
        print(j,end='')
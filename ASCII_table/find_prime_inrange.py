 
low_limit,high_limit = input('Enter number to (start,end): ').split(',')
prime = []

for num in range(int(low_limit),int(high_limit)+1):
    for i in range(2,num):
        print(num,i,end=' ')
    print()


def star_pyramid(num):
      for i in range(num+1):
        print("*"*i)


def num_pyramid(num):
    for i in range(1,num+1):
        for j in range(1,i+1):
            print(j,end='')
        print()
  

n = int(input('Enter a number: '))
# num_pyramid(n) 
star_pyramid(n)

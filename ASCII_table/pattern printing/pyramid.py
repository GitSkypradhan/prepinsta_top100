
def star_pyramid(num):
      for i in range(num+1):
        print("*"*i)


def num_pyramid(num):
    for i in range(1,num+1):
        for j in range(1,i+1):
            print(j,end='')
        print()
  
def reverse_pyramid(num):
    # for i in range(num,0,-1):
    #     for j in range(1,i+1):
    #         print(j,end='')
    #     print()
    for i in range(1,num+1):
        for j in range(1,num+2-i):
            print(j,end='')
        print()

def triangle_pyramid(num):
    for i in range(1,num+1):
        print("o"*(num+i),end='')  
        print()


n = int(input('Enter a number: '))
# num_pyramid(n) 
# star_pyramid(n)
# reverse_pyramid(n)

triangle_pyramid(n)

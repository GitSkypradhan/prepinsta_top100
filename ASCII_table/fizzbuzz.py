# def fizzbuzz():
#     for num in range(1,101):
#         if num%3==0 and num%5==0:
#             print("FizzBuzz")
#         elif num%5==0:
#             print('Fizz')
#         elif num%3==0 :
#             print('Buzz')
#         else:
#             print(num)

def fizzbuzz():
         for num in range(1,101):
            if num%3==0:print("Fizz",end='')
            if num%5==0:print("Buzz");continue
            if num%3==0:print();continue
            print(num)
 
 

fizzbuzz()
print("har har mahadev")

# method 1

user_num = int(input("Enter any number: "))

try:
    if user_num <0:
        print(user_num,"is a negative integer")
    elif user_num >0:
        print(user_num,'is a postive integer')
    else:
        print("The integer is Zero")
except:
    pass


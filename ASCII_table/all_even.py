def all_even(num1:int,num2:int,res=[]) -> None:
        res = [num for num in range(num1,num2+1) if num%2==0 ]
        return res

print(all_even(10,20))


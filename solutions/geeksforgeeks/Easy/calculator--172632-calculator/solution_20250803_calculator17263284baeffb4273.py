class Solution:
    def calculate(self, a: int, b: int, operator: int) -> None:
        if operator==1:
            result = a+b
        elif operator==2:
            result = a-b
        elif operator==3:
            result = a*b
        else:
            result = "Invalid Input"
        print(result,end='')

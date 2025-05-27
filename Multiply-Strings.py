class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def to_int(number):
            num = 0
            for i in number:
                num = num * 10 + int(i)
            return num
        
        return str(to_int(num1) * to_int(num2))
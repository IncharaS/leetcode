class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next_number(h):
            num = 0
            while h > 0:
                digit = h % 10
                num += (digit**2)
                h //= 10
            return num
        
        set_numbers = set()
        
        while n != 1 and n not in set_numbers:
            set_numbers.add(n)
            n = get_next_number(n)
        
        return True if n == 1 else False 
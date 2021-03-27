class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        digit = ['0','1','2','3','4','5','6','7','8','9']
        times1, times2 = 1, 1
        first, second = 0, 0
        
        for letter in num1[::-1]:
            n = digit.index(letter)
            first += n * times1
            times1 *= 10
          
        for letter in num2[::-1]:
            n = digit.index(letter)
            second += n * times2
            times2 *= 10
        
        return str(first*second)
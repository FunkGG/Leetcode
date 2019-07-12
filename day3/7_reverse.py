class Solution:
    def reverse(self, x: int) -> int:
        maxValue = (1<<31) - 1 if x>0 else 1<<31
        res = abs(x)
        y = 0
        while res!= 0:
            y = y*10 + res%10
            if y > maxValue:
                return 0
            res = res//10
        return y if x>0 else -y

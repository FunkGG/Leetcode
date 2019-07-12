class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        if x < 10:
            return True
        if x % 10 == 0:
            return False
        y=0
        while x:
            y=y*10+x%10
            x=x//10
            if y>x:
                return False
            if y == x:
                return True
            if y == x//10 and y:
                return True

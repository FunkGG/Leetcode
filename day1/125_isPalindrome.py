class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = filter(str.isalnum,s)
        list1 = [i for i in s]
        s = ''.join(list1).lower()
        if s == s[::-1]:
            return True
        else:
            return False

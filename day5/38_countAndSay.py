class Solution:
    def countAndSay(self, n: int) -> str:
        if n > 1:
            return self.Say(self.countAndSay(n-1))
        else:
            return '1'
    def Say(self,nums):
        i = 0
        tmp = nums[0]
        out = ''
        for num in nums:
            if num == tmp:
                i += 1
            else:
                out += str(i) + tmp
                i = 1
                tmp = num
        out += str(i) + tmp
        return out

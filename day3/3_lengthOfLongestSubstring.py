class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left = 0
        Dicts = {}
        for i, value in enumerate(s):
            if value in Dicts:
                index = Dicts[value]+1
                if index > left:
                    left = index
            nums = i - left + 1
            res = max(res, nums)
            Dicts[value] = i
        return res

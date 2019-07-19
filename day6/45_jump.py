class Solution:
    def jump(self, nums: List[int]) -> int:
        numsLb = [i+j for i,j in enumerate(nums)]
        i = 0
        stp = 0
        n = len(nums)
        while i < n-1:
            if nums[i]+i >= n-1:
                return stp+1
            s = numsLb[i + 1:i + nums[i] + 1]
            i = s.index(max(s))+i+1
            stp += 1
        return stp

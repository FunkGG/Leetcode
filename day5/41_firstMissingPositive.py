class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        if not nums or nums[0] > 1 or nums[-1] < 1:
            return 1
        out = nums[-1]+1
        for i in range(len(nums)-1):
            if nums[i+1] > 1 and nums[i+1] - nums[i] > 1:
                num = nums[i] + 1
                if num < 1:
                    num = 1
                return num
        return out

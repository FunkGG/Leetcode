class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        out = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            num = nums[i]
            numsNew = nums[:]
            numsNew.pop(i)
            out += [[num] + i for i in self.permuteUnique(numsNew)]
        return out  

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        out = []
        for i in range(len(nums)):
            num = nums[i]
            numsNew = nums[:]
            numsNew.pop(i)
            out += [[num] + i for i in self.permute(numsNew)]
        return out

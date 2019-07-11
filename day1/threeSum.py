class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i, num1 in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if num1 > 0:
                break
            left = i + 1
            right = n - 1
            while left < right and nums[right]+1:
                sumThree = nums[i] + nums[left] + nums[right]
                if sumThree == 0:
                    tmp = [nums[i],nums[left],nums[right]]
                    res.append(tmp)
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif sumThree > 0:
                    right -= 1
                else:
                    left += 1
        return res

class Solution:
    def BubbleSort(self, nums: List[int]) -> List[int]]:
        n = len(nums)
        if n == 0:
            return nums
        for i in range(n):
            for j in range(n-1-i):
                if nums[j] > nums[j+1]:
                    tmp = nums[j+1]
                    nums[j+1] = nums[j]
                    nums[j] = tmp
        return nums
        

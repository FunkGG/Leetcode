class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        i = 0
        j = n-1
        if nums[i]<nums[j]:
            return nums[i]
        while i < j:
            mid = (i+j+1)//2
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            if nums[mid] > nums[0]:
                i = mid
            else:
                j = mid

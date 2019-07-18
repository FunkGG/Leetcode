class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = -1 
        r = len(nums)
        while l< r-1:
            mid = int((l+r)/2+0.5)
            if target < nums[mid]:
                r = mid
            elif target > nums[mid]:
                l = mid
            else:
                return mid
        return r

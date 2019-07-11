class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if not n:
            return -1
        l = 0
        r = n-1
        out = -1
        if target == nums[0]:
                return 0
        if target == nums[-1]:
                return n-1
        if target > nums[0]:
            while l < r-1:
                mid = (l+r+1)//2
                if target > nums[mid] >= nums[0]:
                    l = mid
                elif target == nums[mid]:
                    out = mid
                    break
                else:
                    r = mid
        elif target < nums[-1]:
            while l < r-1:
                mid = (l + r + 1) // 2
                if target < nums[mid] <= nums[-1]:
                    r = mid
                elif target == nums[mid]:
                    out = mid
                    break
                else:
                    l = mid
        return out

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l1 = -1
        r2 = len(nums)
        while l1 < r2-1:
            mid = (l1 + r2 + 1)//2
            if nums[mid] < target:
                l1 = mid
            elif nums[mid] > target:
                r2 = mid
            else:
                r1 = l2 = mid
                while l1 < r1-1 or l2 < r2-1:
                    if l1 < r1-1:
                        mid1 = (l1 + r1 + 1) // 2
                        if nums[mid1] != target:
                            l1 = mid1
                        elif nums[mid] == target:
                            r1 = mid1
                    if l2 < r2-1:
                        mid2 = (l2 + r2 + 1) // 2
                        if nums[mid2] != target:
                            r2 = mid2
                        elif nums[mid2] == target:
                            l2 = mid2
                return [r1, l2]
        return [-1, -1]

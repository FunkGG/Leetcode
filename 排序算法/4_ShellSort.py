class Solution:
    def SelectionSort(self, nums: List[int]) -> List[int]]:
        n = len(nums)
        if not n:
            return nums
        gap = n//2
        while gap:
            for i in range(gap,n):
                tmp = nums[i]
                j = i-gap
                while j > 0 and tmp < nums[j]:
                    nums[j+gap] = nums[j]
                    j -= gap
                nums[j+gap] = tmp
            gap = gap//2
        return nums

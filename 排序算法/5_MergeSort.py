class Solution:
    def MergeSort(self, nums: List[int]) -> List[int]]:
        n = len(nums)
        if n < 2:
            return nums
        mid = n // 2
        left = self.MergeSort()

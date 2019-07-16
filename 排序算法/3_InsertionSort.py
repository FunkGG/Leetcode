class Solution:
    def SelectionSort(self, nums: List[int]) -> List[int]]:
        n = len(nums)
        if not n:
            return nums
        for i in range(1,n):
            tmp = nums[i]
            j = i-1
            while nums[j]>tmp and j>0:
                nums[j+1]=nums
                j -= 1
            nums[j] = tmp
        return nums

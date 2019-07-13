class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def f(i):
            for j in range(i + 1, len(nums)):
                if j == len(nums)-1 or nums[i] >= nums[j + 1]:
                    tmp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = tmp
                    nums[i+1:]=sorted(nums[i+1:])
                    break
            
        l = len(nums)
        i=0
        k = 1
        for i in range(l-2, -1, -1):
            if nums[i] < nums[i+1]:
                f(i)
                k=0
                break
        if k:
            nums.reverse()

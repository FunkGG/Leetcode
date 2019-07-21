class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        left = self.maxSubArray(nums[:n//2])
        right = self.maxSubArray(nums[n//2:])
        midLeft = nums[n//2-1]
        tmp = 0
        for i in range(n//2-1,-1,-1):
            tmp += nums[i]
            midLeft = max(tmp, midLeft)
        midRight = nums[n//2]
        tmp = 0
        for i in range(n//2, n):
            tmp += nums[i]
            midRight = max(tmp, midRight)
        return max(left,right,midLeft+midRight)

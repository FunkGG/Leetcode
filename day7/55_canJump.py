class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if 0 in nums:
            i = 0
            j = 1
            n = len(nums)
            while i < n-1:
                tmp = i
                while j<= i+nums[i]:
                    if j == n-1:
                        return True
                    if nums[j]+j >= nums[tmp]+tmp:
                        tmp = j
                    j += 1
                i = tmp
                if nums[tmp] == 0:
                    return False
                j = i+1
        return True

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = float('inf')
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = n-1
            while left<right:
                tmp = nums[i]+nums[left]+nums[right]
                if tmp == target:
                    return target
                if abs(ans-target) > abs(tmp-target):
                    ans = tmp
                if tmp > target:
                    right -= 1
                else:
                    left += 1
        return ans

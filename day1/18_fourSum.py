class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        out = []
        for i, num1 in enumerate(nums):
            if i>0 and num1 == nums[i-1]:
                continue
            for j in range(i+1, n):
                if j-i>1 and nums[j] == nums[j-1]:
                    continue
                num2 = nums[j]
                sum12 = num1 +num2
                left = j+1
                right = n-1
                while left<right:
                    tmp = sum12 + nums[left] +nums[right]
                    if tmp == target:
                        out.append([num1, num2, nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif tmp > target:
                        right -= 1
                    else:
                        left += 1
        return out       

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        n = len(nums)
        j = n-1
        i = 0
        while i <= j:
            if nums[i] != val:
                i += 1
            elif nums[j] != val:
                nums[i] = nums[j]
                j -= 1
                i +=1
            else:
                j -= 1
        return j+1

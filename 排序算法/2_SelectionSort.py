class Solution:
    def SelectionSort(self, nums: List[int]) -> List[int]]:
        n = len(nums)
        if not n:
            return nums
        for i in range(n-1):
            ans = -1
            for j in range(i,n):
                if ans < 0:
                    ans = j
                elif nums[j] < nums[ans]:
                    ans = j
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
        return nums
            
        

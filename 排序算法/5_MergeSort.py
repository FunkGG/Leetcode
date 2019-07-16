class Solution:
    def MergeSort(self, nums: List[int]) -> List[int]]:
        n = len(nums)
        if n < 2:
            return nums
        mid = n // 2
        return self.merge(self.MergeSort(nums[:mid]), self.MergeSort(nums[mid:])
    
    def merge(self,num1,num2):
        out = []
        i = 0
        j = 0
        while i<len(num1) and j<len(num2):
            if nums1[i] <= nums2[j]:
                out.append(nums1[i])
                i += 1
            else:
                out.append(nums2[j])
                j += 1
        if i < len(num1):
                out += num1[i:len(num1)]
        elif j < len(num2):
                out ++ num2[j:len(num2)]
        return out

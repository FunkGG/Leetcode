class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        if m < n:
            return self.findMedianSortedArrays(nums2, nums1)
        half = (m + n)//2
        i = m//2
        j = half - i
        min1 = nums1[i-1] if i > 0 else float('-inf')
        max1 = nums1[i] if i < m else float('inf')
        min2 = nums2[j-1] if j > 0 else float('-inf')
        max2 = nums2[j] if j < n else float('inf')
        left = half - n
        right = m-(left)
        while True:
            if min1 > max2:
                i = (i + left) // 2
                right = half - j
            elif min2 > max1:
                i = int((i + right) / 2 + 0.5)
                left = half - j
            else:
                break
            j = half - i
            min1 = nums1[i - 1] if i > 0 else float('-inf')
            max1 = nums1[i] if i < m else float('inf')
            min2 = nums2[j - 1] if j > 0 else float('-inf')
            max2 = nums2[j] if j < n else float('inf')
        if (m + n) % 2 == 0:
            return (max(min1, min2) +min(max1, max2)) / 2
        else:
            return min(max1, max2)

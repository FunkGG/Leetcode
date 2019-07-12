class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        leftH = height[left]
        rightH = height[right]
        area = (right-left)*min(leftH, rightH)
        while left < right-1:
            if leftH < rightH:
                left += 1
                if height[left] <= leftH:
                    continue
            else:
                right -= 1
                if height[right] <= rightH:
                    continue
            leftH = height[left]
            rightH = height[right]
            area =max(area, (right-left)*min(leftH, rightH))
        return area

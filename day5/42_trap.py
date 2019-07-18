class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        i = 0
        j = n-1
        left =  height[i]
        right = height [j]
        h = min(left, right)
        out = 0
        while i < j:
            if left <= right:
                i += 1
                left = height[i]
                if left < h:
                    out += h - left
                else:
                    h = min(left, right)
            else:
                j -= 1
                right = height[j]
                if right < h:
                    out += h - right
                else:
                    h = min(left, right)
        return out

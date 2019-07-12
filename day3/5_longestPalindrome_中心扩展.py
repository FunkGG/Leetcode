class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s =="":
            return s
        res = 1
        rstr=s[-1]
        length = len(s)
        step = (res - 1) // 2
        for i in range(length - 1):
            stp = i - step
            edp = i + 1 + step
            if edp > length-1:
                break
            a = s[stp:edp+1]
            a = a[::-1]
            if s[stp:edp+1] == a:
                while stp > 0 and edp < (length - 1) and s[stp-1] == s[edp+1]:
                    stp -= 1
                    edp += 1
                if (edp - stp + 1) > res:
                    res = (edp - stp + 1)
                    step = (res-1) // 2
                    rstr = s[stp:edp+1]

            stp = i - step
            edp = i + 2 + step
            if edp > (length - 1):
                break
            a = s[stp:edp+1]
            a = a[::-1]
            if s[stp:edp+1] == a:
                while stp > 0 and edp < (length - 1)and s[stp-1] == s[edp+1]:
                    stp -= 1
                    edp += 1
                if (edp - stp + 1) > res:
                    res = (edp - stp + 1)
                    step = (res-1) // 2
                    rstr = s[stp:edp + 1]
        return rstr

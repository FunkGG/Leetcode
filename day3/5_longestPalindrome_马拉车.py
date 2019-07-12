class Solution:
    def longestPalindrome(self, s: str) -> str:
        mana = ''
        for i in range(2 * len(s) + 1):
            if i % 2 == 1:
                mana += s[i // 2]
            else:
                mana += '#'
        p = []
        rightMax = -1
        rightMaxCenter = -1
        for i in range(len(mana)):
            left = right = i
            if i <= rightMax:
                j = 2 * rightMaxCenter - i
                pl = j - p[j] + 1
                cl = 2*rightMaxCenter-rightMax
                if cl < pl:
                    p.append(p[j])
                    continue
                if cl > pl:
                    p.append(rightMax+1-i)
                    continue
                else:
                    left = i - p[j] + 1
                    right = i + p[j] -1
            while left>0 and right<len(mana)-1:
                if mana[left-1] == mana[right+1]:
                    left -= 1
                    right += 1
                else:
                    break
            p.append(right+1-i)
            rightMax = right
            rightMaxCenter = i
        maxp = max(p)
        index = p.index(maxp)
        out = mana[index-maxp+1:index+maxp]
        return out.replace('#','')

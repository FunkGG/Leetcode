class Solution:
    def romanToInt(self, s: str) -> int:
        d =  {'M':1000, 'CM': 900, 'D': 500, 'CD': 400, 
                'C':100, 'XC':90, 'L':50, 'XL':40,
                'X':10, 'IX': 9, 'V':5, 'IV':4,
                'I':1}
        i = 0
        ans = 0
        while i < len(s):
            if i+1<len(s) and s[i]+s[i+1] in d:
                ans += d[s[i]+s[i+1]]
                i += 2
            else:
                ans += d[s[i]]
                i += 1
        return ans

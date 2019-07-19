class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = 0 
        j = 0 
        start = -1
        match = 0
        while i < len(s):
            if j < len(p) and (s[i] == p[j] or p[j] == '?') :
                i += 1
                j += 1 
            elif j < len(p) and p[j] == '*' :
                start = j
                match = i
                j += 1 
            elif start != -1 :
                j = start + 1  
                match += 1
                i = match 
            else :
                return False 
        
        for x in p[j:] :
            if x != '*' :
                return False
        return True

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return []
        l = len(words[0])
        sumlen = 0
        wdsnum = {}
        for word in words:
            if word in wdsnum:
                wdsnum[word] += 1
            else:
                wdsnum[word] = 1
            sumlen += l
        out = []
        p = 0
        while p <= len(s)-sumlen:
            i = p
            wordcopy = wdsnum.copy()
            while wordcopy:
                if s[i:i+l] in wordcopy:
                    wordcopy[s[i:i+l]] -= 1
                    if wordcopy[s[i:i+l]] == 0:
                        wordcopy.pop(s[i:i+l])
                    i += l
                else:
                    break
            if not wordcopy:
                out.append(p)
            p += 1
        return out

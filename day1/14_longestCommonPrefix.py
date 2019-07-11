class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        srs = [i for i in zip(*strs)]
        i=-1
        for i, sr in enumerate(srs):
            if len(set(sr)) != 1:
                i -= 1
                break
        if strs[0]:
            return strs[0][0:i+1]
        else:
            return ''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = {}
        for sr in strs:
            srl = list(sr)
            srl.sort()
            srl = tuple(srl)
            if srl in s:
                s[srl].append(sr)
            else:
                s[srl]=[sr]
        return [i for i in s.values()]

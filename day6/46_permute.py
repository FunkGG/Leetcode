class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = [[]]
        for num in nums:
            while num not in out[0]:
                tmp = out.pop(0)
                for i in range(len(tmp)+1):
                    tmp.insert(i,num)
                    out.append(tmp[:])
                    tmp.pop(i)
        return out

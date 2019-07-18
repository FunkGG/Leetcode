class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        if not n:
            return []
        candidates.sort()
        out = []
        def f(tmplist,tmpSum,i):
            if tmpSum == target:
                out.append(tmplist)
            else:
                for j in range(i,n):
                    candidate = candidates[j]
                    if tmpSum+candidate>target:
                        break
                    if j>i and candidate == candidates[j-1]:
                        continue
                    f(tmplist+[candidate], tmpSum+candidate, j+1)
        f([],0,0)
        return out

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        if not n:
            return []
        out = []
        def f1(tmplist, tmpSum, i):
            if target == tmpSum:
                out.append(tmplist)
            else:
                for j in range(i,n):
                    c = candidates[j]
                    if tmpSum+c>target:
                        break
                    f1(tmplist+[c],tmpSum+c,j)
        f1([],0,0)
        return out

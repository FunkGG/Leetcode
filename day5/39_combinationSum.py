class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        out = []
        tmplist = []
        # ans = target
        def f1(tmplist, target, stp):
            if target == 0:
                out.append(tmplist)
            if target >= candidates[0]:
                for i in range(stp, n):
                    candidate = candidates[i]
                    f1(tmplist+[candidate], target-candidate, i)
        f1(tmplist, target, 0)
        return out

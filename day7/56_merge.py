class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        out = []
        tmp = intervals.pop(0)
        while intervals:
            ans = intervals.pop(0)
            if ans[0] > tmp[1]:
                out.append(tmp)
                tmp = ans
            elif ans[1] > tmp[1]:
                tmp[1] = ans[1]
        out.append(tmp)
        return out

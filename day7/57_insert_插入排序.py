class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        i = intervals.index(newInterval)
        a = []
        if i < len(intervals) - 1:
            a = intervals[i + 1]
        while a and newInterval[1] >= a[0]:
            if newInterval[1] <= a[1]:
                newInterval[1] = a[1]
                intervals.pop(i + 1)
                break
            else:
                intervals.pop(i + 1)
                if i < len(intervals) - 1:
                    a = intervals[i + 1]
                else:
                    break
        b = []
        if i:
            b = intervals[i - 1]
        if b and newInterval[0] <= b[1]:
            if newInterval[1] > b[1]:
                b[1] = newInterval[1]
                intervals.pop(i)
            else:
                intervals.pop(i)
        return intervals

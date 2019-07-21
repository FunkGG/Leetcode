class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        while i < len(intervals):
            interval = intervals[i]
            if newInterval[0] > interval[1]:
                i += 1
                continue
            if newInterval[1] < interval[0]:
                intervals.insert(i,newInterval)
                return intervals
            if newInterval[0] < interval[0]: 
                interval[0] = newInterval[0]
            if newInterval[1] <= interval[1]:
                return intervals
            else:
                interval[1] = newInterval[1]
                newInterval = intervals.pop(i)
        intervals.append(newInterval)
        return intervals

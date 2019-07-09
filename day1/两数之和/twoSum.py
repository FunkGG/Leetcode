class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}
        for i in range(len(nums)):
            num = nums[i]
            res = target - num
            if res in numsDict.keys():
                return i, numsDict[res]
            else:
                numsDict[num] = i

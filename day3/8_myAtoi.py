class Solution:
    def myAtoi(self, str: str) -> int:
        str=str.lstrip()
        ans = 0
        if not str:
            return ans
        sign = 1
        if str[0] == '-':
            sign = -1
            str = str[1:]
        elif str[0] == '+':
            str = str[1:]
        numDict = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        for i in str:
            if i in numDict:
                ans = ans*10 + numDict[i]
            else:
                break
        return min(max(ans*sign, -(1<<31)), (1<<31)-1)

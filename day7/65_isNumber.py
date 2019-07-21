class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()  #去掉开头的空格
        if not s:
            return False
        n = len(s)
        nums = ['0','1','2','3','4','5','6','7','8','9']
        e = ['e']
        point = ['.']
        signs = ['+','-']
        sign = 1  # 表示在数字开头，可以出现正负号
        num = 0
        for i, cha in enumerate(s):
            if sign:
                if cha not in nums+point+signs:
                    return False
                if cha in signs:
                    if i+1 == n:  # 只有一个正负符号，返回False
                        return False
                if cha in point: # 判断小数点之前或之后是否是数字
                    if i+1 == n:  
                        return False
                    if s[i+1] not in nums:
                        return False 
                    point.pop()   # 小数点只能出现一次
                sign = 0
            else:
                if cha not in nums+point+e:
                    return False
                if cha in point: # 判断小数点之前或之后是否是数字
                    if s[i-1] not in nums: 
                        if i+1 == n:
                            return False
                        if s[i+1] not in nums:
                            return False
                    point.pop()
                if cha in e:  
                    if i+1 == n:
                        return False
                    if s[i-1] not in nums+['.']:
                        return False
                    e.pop()
                    if point:
                        point.pop()
                    sign = 1
        return True

# -leetcode刷题记录
##day1
859.亲密字符串
题解：首先判断字符串A、B长度是否相等，然后判断A、B是否相等。如果相等，判断A中是否有相同元素；如果不等，判断能否交换两个字母使A、B相等
代码：
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        m = len(A)
        n = len(B)
        if m!=n:
          return False
        if A==B:
            if len(set(A)) == m:
                return False
            else:
                return True 
        tmp=0
        a = []
        b = []
        for i in range(m):
            if A[i] != B[i]:
                a.append(A[i])
                b.append(B[i])
                tmp += 1
                if tmp == 2:
                    if A[i+1:] == B[i+1:]:
                        break
                    else:
                        return False
        if a[0] == b[1] and a[1] == b[0]:
            return True            
        return False


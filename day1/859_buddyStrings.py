class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        m = len(A)
        n = len(B)
        if A==B:
            if len(set(A)) == m:
                return False
            else:
                return True 
        tmp=0
        a = []
        b = []
        if m == n:
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

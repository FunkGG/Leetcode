class Solution:
    def intToRoman(self, num: int) -> str:
        s = ''
        roman = [['V', 'I'], ['L', 'X'], ['D', 'C'],['', 'M']]
        for i in range(3, -1, -1):
            div = 10 ** i
            ans = num // div
            num = num % div
            if ans == 9:
                s += (roman[i][1] + roman[i + 1][1])
                continue
            if ans > 4:
                s += (roman[i][0])
                ans -= 5
            if ans == 4:
                s += (roman[i][1] + roman[i][0])
            else:
                s += (roman[i][1] * ans)
        return s

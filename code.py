class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        s = s[::-1]
        if s[-1] == '-':
            s = s[:-1]
            s = '-'+s
        x = int(s)
        if -2**31 <= x <= 2**31 - 1:
            return x
        return 0

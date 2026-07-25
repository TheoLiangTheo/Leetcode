class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x *= -1
            if -1*int(''.join(list(str(x))[::-1])) < -2**31:
                return 0
            return -1*int(''.join(list(str(x))[::-1]))
        if int(''.join(list(str(x))[::-1])) > 2**31 - 1:
            return 0
        return int(''.join(list(str(x))[::-1]))
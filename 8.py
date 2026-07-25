class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0: return 0
        s = list(s)
        new = ''
        positive = True
        change = True
        for i in range(len(s)):
            if s[i] != ' ':
                break
        s = s[i:]
        for i in range(len(s)):
            if s[i] in '0123456789':
                new += s[i]
                change = False
            elif s[i] == '-':
                if change:
                    positive = False
                    change = False
                else:
                    break
            elif s[i] == '+':
                if change:
                    change = False
                else:
                    break
            else:
                break
        if len(new) == 0 or int(new) == 0:
            return 0
        new = int(new)
        if positive:
            if new > 2**31 - 1:
                new = 2**31 - 1
            return new
        else:
            if new > 2**31:
                new = 2**31
            return new*-1
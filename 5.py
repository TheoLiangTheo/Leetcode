def isPalindrome(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            return False
    return True
class Solution:
    def longestPalindrome(self, s: str) -> str:
        long = ''
        for i in range(len(s)):
            current = ''
            for j in range(i,len(s)):
                current += s[j]
                if isPalindrome(current):
                    if len(current) > len(long):
                        long = current
                    if j == len(s)-1:
                        return long

        return long
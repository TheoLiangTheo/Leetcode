class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = ''
        for i in range(len(s)):
            visited = []
            current = ''
            for j in range(i,len(s)):
                l = s[j]
                if l in visited:
                    break
                current += l
                visited.append(l)
            if len(current) > len(ans):
                ans = current
        return len(ans)
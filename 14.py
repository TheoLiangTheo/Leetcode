class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        counts = []
        for i in range(len(strs)):
            counts.append(len(strs[i]))
        if max(counts) == 0:
            return ''
        for i in range(min(counts)):
            current = strs[0][i]
            for j in range(1,len(strs)):
                if strs[j][i] != current:
                    return ans
            ans += current
        return ans
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        mappings = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        ans = []

        def dfs(s, path):
            if len(s) == 0:
                ans.append(''.join(path))
                return
            for i in range(len(mappings[int(s[0]) - 2])):
                dfs(s[1:], path + [mappings[int(s[0]) - 2][i]])
            return

        dfs(digits, [])
        return ans

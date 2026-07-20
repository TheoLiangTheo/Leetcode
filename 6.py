class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        mydict = {}
        for i in range(numRows):
            mydict[i] = []
        upordown = 'd'
        row = 0
        for i in range(len(s)):
            mydict[row].append(s[i])
            if upordown == 'd':
                if row == numRows - 1:
                    row = numRows -2
                    upordown = 'u'
                else:
                    row += 1
            else:
                if row == 0:
                    row = 1
                    upordown = 'd'
                else:
                    row -= 1
        final = ''
        for key in mydict:
            final += ''.join(mydict[key])
        return final
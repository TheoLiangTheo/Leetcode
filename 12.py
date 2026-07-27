romans = [None,None,'M','D','C','L','X','V','I']
class Solution:
    def intToRoman(self, num: int) -> str:
        num = str(num)
        num = (4-len(num))*'0'+num
        ans = ''
        for i in range(4):
            current = int(num[i])
            if current == 1:
                ans += romans[i*2+2]
            elif current == 2:
                ans += 2*romans[i*2+2]
            elif current == 3:
                ans += 3*romans[i*2+2]
            elif current == 4:
                ans += romans[i*2+2]+romans[i*2+1]
            elif current == 5:
                ans += romans[i*2+1]
            elif current == 6:
                ans += romans[i*2+1]+romans[i*2+2]
            elif current == 7:
                ans += romans[i*2+1]+2*romans[i*2+2]
            elif current == 8:
                ans += romans[i*2+1]+3*romans[i*2+2]
            elif current == 9:
                ans += romans[i*2+2]+romans[i*2]
        return ans
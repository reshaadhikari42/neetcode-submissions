class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ''
        for each in strs:
            res += str(len(each))
            res += '#'
            res += each
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        num = ''
        i = 0
        while i < len(s):
            string = ''  # resetting for new string
            num = ''  # reseting for new string
            
            while s[i].isdigit() and s[i] != '#':
                num += s[i]
                i += 1
            i += 1  # to move out of hash to actual string
            
            for j in range(int(num)):
                string += s[i + j]

            res.append(string)
            i = i + int(num)
        
        return res
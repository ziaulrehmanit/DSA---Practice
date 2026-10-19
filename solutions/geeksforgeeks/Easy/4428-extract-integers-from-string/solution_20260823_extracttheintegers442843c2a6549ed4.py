class Solution:
    def extractInt(self, s: str) -> list[str]:
        ans = []
        num = ""

        for ch in s:
            if '0' <= ch <= '9':
                num += ch
            else:
                if num:
                    ans.append(num)
                    num = ""

        if num:
            ans.append(num)

        return ans

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        HashMap = {}
        for i in magazine:
            HashMap[i] = HashMap.get(i, 0) + 1
        for i in ransomNote:
            if i not in HashMap:
                return False
            else:
                HashMap[i] -= 1
                if HashMap[i] == 0:
                    del HashMap[i]
        return True

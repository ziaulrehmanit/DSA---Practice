class Solution:
    def checkEqual(self, a, b) -> bool:
        HashMap = {}
        for num in a:
            if num in HashMap:
                HashMap[num] += 1
            else:
                HashMap[num] = 1
        for num in b:
            if num in HashMap and HashMap[num] > 0:
                HashMap[num] -= 1
            else:
                return False
        return True

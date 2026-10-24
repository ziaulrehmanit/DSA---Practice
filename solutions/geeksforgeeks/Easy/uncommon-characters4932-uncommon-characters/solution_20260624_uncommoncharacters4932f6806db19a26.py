class Solution:
    def uncommonChars(self, s1, s2):
        set1 = set(s1)
        set2 = set(s2)

        uncommon = set1.symmetric_difference(set2)

        return ''.join(sorted(uncommon))

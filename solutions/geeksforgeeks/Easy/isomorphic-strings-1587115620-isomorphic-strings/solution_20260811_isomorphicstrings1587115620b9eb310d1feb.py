class Solution:
    def areIsomorphic(self, s1, s2):
        m1, m2 = [0] *256, [0] *256
        for i in range(len(s1)):
            if m1[ord(s1[i])] != m2[ord(s2[i])]:
                return False
            m1[ord(s1[i])] = i + 1
            m2[ord(s2[i])] = i + 1
        return True

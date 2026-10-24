class Solution:
    def areAnagrams(self, s1, s2):
       
        if len(s1)!=len(s2):
            return False
        
        count=[0]*26
        for i in range(len(s1)):
            count[ord(s1[i])-97]+=1
            count[ord(s2[i])-97]-=1
            
        return all(c==0 for c in count)

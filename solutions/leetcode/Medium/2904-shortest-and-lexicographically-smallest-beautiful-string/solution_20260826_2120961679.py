class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        mini = 101
        res = ""
        for i in range(len(s)):
            cnt = 0
            for j in range(i, len(s)):
                if s[j] =='1':
                    cnt += 1
                if cnt == k:
                    current_len = j - i + 1
                    current_sub = s[i:j+1]
                    if current_len < mini:
                        mini = current_len
                        res = current_sub
                    elif current_len == mini and current_sub < res:
                        res = current_sub
                    break
        return res

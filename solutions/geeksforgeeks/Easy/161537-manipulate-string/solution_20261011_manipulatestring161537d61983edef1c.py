def manipulateIt(s):
    ans = ""
    n = len(s)
    for i in range(0, n, 2):
        char = s[i]
        shift = int(s[i+1])
        
        new_pos = ((ord(char) - 97) + shift) % 26 
        new_char = chr(97 + new_pos)
        
        ans += new_char
        
    return ans

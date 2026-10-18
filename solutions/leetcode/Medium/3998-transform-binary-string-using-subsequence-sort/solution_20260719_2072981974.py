class Solution:
    def transformStr(self, s: str, strs: List[str]) -> List[bool]:
        p = [i for i, char in enumerate(s) if char == '0']
        total_zeros = len(p)
        ans = []
        for t in strs:
            fixed_zeros = [i for i, char in enumerate(t) if char == '0']
            questions = [i for i, char in enumerate(t) if char == '?']
            needed = total_zeros - len(fixed_zeros)
            if needed < 0 or needed > len(questions):
                ans.append(False)
                continue
            chosen_from_q = questions[:needed]
            q = sorted(fixed_zeros + chosen_from_q)
            possible = True
            for i in range(total_zeros):
                if p[i] < q[i]:
                    possible = False
                    break
            ans.append(possible)
        return ans

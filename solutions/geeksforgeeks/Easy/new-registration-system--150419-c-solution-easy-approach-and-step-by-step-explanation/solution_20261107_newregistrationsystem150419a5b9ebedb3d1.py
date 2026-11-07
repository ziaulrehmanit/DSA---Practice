class Solution:
    def generateUsernames(self, arr: list[str]) -> list[str]:
        reserved = set(arr)
        assigned = set()
        suffix_map = {}

        result = []

        for name in arr:
            if name not in assigned:
                assigned.add(name)
                result.append(name)
            else:
                k = suffix_map.get(name, 1)

                while True:
                    candidate = f"{name}{k}"
                    if candidate not in reserved and candidate not in assigned:
                        break
                    k += 1

                suffix_map[name] = k + 1

                assigned.add(candidate)
                result.append(candidate)

        return result

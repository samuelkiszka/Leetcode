class Solution:
    def minOperations(self, logs: List[str]) -> int:
        m = 0
        for l in logs:
            if l[0:2] == "..":
                m = 0 if m == 0 else m - 1
            elif l[0] == '.':
                pass
            else:
                m += 1
        return m
                
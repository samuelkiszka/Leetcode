class Solution:
    def minOperations(self, logs: List[str]) -> int:
        m = 0
        for l in logs:
            if l == "../":
                if m > 0:
                    m -= 1
            elif l == "./":
                pass
            else:
                m += 1
        return m
                
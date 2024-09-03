class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m*n:
            return []
        out = [[] for _ in range(m)]
        i = 0
        while i < m:
            out[i] = original[i*n: i*n+n]
            i += 1
        return out
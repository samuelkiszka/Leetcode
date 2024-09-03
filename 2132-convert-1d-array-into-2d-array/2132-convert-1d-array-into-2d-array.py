class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m*n:
            return []
        out = [[] for _ in range(m)]
        for r in range(m):
            out[r] = original[r*n: r*n+n]
        return out
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        cnt = len(original)
        if original == [] or cnt != m*n:
            return []
        out = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                out[r][c] = original[r*n+c]
        return out
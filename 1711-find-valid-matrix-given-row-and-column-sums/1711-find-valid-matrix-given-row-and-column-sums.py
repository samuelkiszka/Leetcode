class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows = len(rowSum)
        cols = len(colSum)
        res = [[0 for _ in range(cols)] for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                cur = min(rowSum[i], colSum[j])
                res[i][j] = cur
                rowSum[i] -= cur
                colSum[j] -= cur

        return res

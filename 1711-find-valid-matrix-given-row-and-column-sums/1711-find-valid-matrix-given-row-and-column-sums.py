class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows = len(rowSum)
        cols = len(colSum)
        res = [[0 for _ in range(cols)] for _ in range(rows)]

        i = 0
        j = 0

        while i < rows and j < cols:
            res[i][j] = min(rowSum[i], colSum[j])
            if rowSum[i] == colSum[j]:
                j += 1
                i += 1
            elif rowSum[i] > colSum[j]:
                rowSum[i] -= colSum[j]
                j += 1
            else:
                colSum[j] -= rowSum[i]
                i += 1
        
        # for i in range(rows):
        #     for j in range(cols):
        #         cur = min(rowSum[i], colSum[j])
        #         res[i][j] = cur
        #         rowSum[i] -= cur
        #         colSum[j] -= cur

        return res

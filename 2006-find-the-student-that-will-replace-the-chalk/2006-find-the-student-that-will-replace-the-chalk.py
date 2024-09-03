class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        last = k % sum(chalk)
        for i in range(len(chalk)):
            last -= chalk[i]
            if last < 0:
                return i
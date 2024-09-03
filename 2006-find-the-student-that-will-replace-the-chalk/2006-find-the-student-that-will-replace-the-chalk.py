class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        last = k % sum(chalk)
        for i, use in enumerate(chalk):
            last -= use
            if last < 0:
                return i
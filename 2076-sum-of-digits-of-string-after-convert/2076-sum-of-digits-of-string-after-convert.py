class Solution:
    def getLucky(self, s: str, k: int) -> int:
        out = 0
        start = ord('a') - 1
        for c in s:
            act = ord(c) - start
            out += act % 10
            out += act // 10
        for i in range(k - 1):
            semi = 0
            tmp = out
            while tmp:
                semi += tmp % 10
                tmp = tmp // 10
            out = semi
        return out